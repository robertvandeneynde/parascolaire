#!/usr/bin/env python3

import argparse

p = argparse.ArgumentParser()
p.add_argument('filename')
p.add_argument('--template')
p.add_argument('--out', help='may contain {lang} tag')
p.add_argument('--out-raw', help='may contain {lang} tag')
a = args = p.parse_args()

assert args.template and args.out and args.out_raw

basefilename = args.filename
template_file = args.template

outfile_format = args.out
outfile_raw_format = args.out_raw

from generate_utils import OutFile

import re

with open(basefilename) as f:
    L = [l.strip('\n') for l in f]

# remove comment line or empty at the beginning
while L and re.compile(r'\s*#?').match(L[0]).group(0) != '':
    del L[0]

if L[0].startswith('"""') or L[0].startswith("'''"):
    sep = '"""' if L[0].startswith('"""') else "'''"
    txt = L[0][3:]
    i = 1
    try:
        while sep not in L[i]:
            txt += L[i] + '\n'
            i += 1
        txt += L[i][:L[i].find(sep)]
    except IndexError:
        pass
    
    def split_head_body(txt):
        empty = re.compile('^\s*$')
        d = txt.split('\n')
        while d and empty.match(d[0]):
            del d[0]
        while d and empty.match(d[-1]):
            del d[-1]
        i = next(
            (i for i,l in enumerate(d)
             if empty.match(l)),
            None)
        if i is None:
            return '', txt 
        else:
            a,b = '\n'.join(d[:i]), '\n'.join(d[i+1:])
            return ('', a) if empty.match(b) else (a,b)
    title, description = split_head_body(txt)
else:
    title, description = '', ''
    i = 0

sections_info = []
while i < len(L):
    if (L[i].startswith('##')
        and ((i+1) < len(L) and L[i+1].startswith('#'))
        and ((i+2) < len(L) and L[i+2].startswith('##'))):
        section_name = L[i+1][1:].strip()
        sections_info.append((i+2, section_name))
        i = i + 3
    else:
        i = i + 1

sections = []
for i, (n1, name) in enumerate(sections_info):
    rang = range(
        n1 + 1,
        sections_info[i+1][0]-2 if (i+1) < len(sections_info) else len(L))
    
    block_info_1 = [
        (j, L[j][2:].strip())
        for j in rang if L[j].startswith('##')
    ]
    
    block_info = [
        (name, range(j+1, j2))
        for (j, name), (j2, name2) in zip(block_info_1, block_info_1[1:])
    ]
    
    if block_info_1:
        block_info.append(
            (block_info_1[-1][1], range(block_info_1[-1][0]+1, rang.stop))
        )
    
    if len(block_info) == 0:
        block_info.append(
            ('', rang)
        )
    else:
        block_info.insert(0,
            ('', range(rang.start, block_info[0][1].start-1))
        )
    
    block_info = [
        (name, rang)
        for name, rang in block_info
        if rang # remove empty rang
    ]
    
    sections.append({
        'name': name,
        'id': name.replace('/', '-').replace(' ', '-'),
        'blocks': [
            {
                'name': block_name,
                'id': name.replace('/', '-').replace(' ', '-') + '-' + str(i+1),
                'title': '',
                'description': '',
                'code': '\n'.join(L[i] for i in block_range),
            }
            for i,(block_name, block_range) in enumerate(block_info)
        ],
    })

from django.conf import settings

settings.configure(TEMPLATES=[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['.'], # if you want the templates from a file
        'APP_DIRS': False, # we have no apps
    },
])

without_extension = lambda x: '.'.join(x.split('.')[:-1]) if '.' in x else x

import django
django.setup()

from django.template import loader
t2 = loader.get_template(template_file)
with OutFile(outfile_format.format(lang='multilang'), 'w') as f:
  f.write(t2.render({
    'lang': '{{fr|en}}',
    'download_link': '{{' + '|'.join(outfile_raw_format.format(lang=l) for l in ('fr', 'en')) + '}}',
    'name': without_extension(args.filename),
    'title': title,
    'description': description,
    'other_langs': [{
        'filename': outfile_format.format(lang='{{en|fr}}'),
        'lang': '{{en|fr}}',
        'text': '{{English here!|Français ici!}}',
    }],
    'sections': sections,
  }))
