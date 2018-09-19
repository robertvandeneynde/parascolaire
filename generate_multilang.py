#!/usr/bin/env python3
from __future__ import print_function

import os, re, shutil, json
import argparse

from generate_utils import OutFileGreen as OutFile

p = argparse.ArgumentParser()
p.add_argument('--files', nargs='*', help='to implement') # TODO to implement
p.add_argument('-l', '--langs', nargs='+')
p.add_argument('--config', nargs='?', default={})
p.add_argument('--print-only', '--dry-run', action="store_true", help="doesn't create file, only print file concerned")
a = args = p.parse_args()

def warning(*args): # orange
    print('\033[33m' + '\aWarning:', *args, '\033[0m')  # \a will BEEEEP or show a notification

def info(*args): # green
    print('\033[32m' + 'Info:', *args, '\033[0m')

def error(*args): # red
    print('\033[31m' + '\aError:', *args, '\033[0m')  # \a will BEEEEP or show a notification

LANGS = args.langs
assert args.print_only or len(LANGS) == 2, "currently only 2 langs"

# TODO: provide metadata file (config file parameter per file/set of file)
if args.config:
    with open(args.config) as f:
        config = json.load(f)
else:
    config = {}
fileinfos = config.get('fileinfos', {})

# Example: bonjour_multilang_as_hello.py
RE = re.compile('''
    ^(.*)                    # filename
    ([._-])multilang         # multilang tag
    (?:(?:\\||_as_)([^.]*))? # name in other lang(s)
    ([.][^.]*)$
''', re.X)
# RE_TR = re.compile('{{(.*?)(?:\|(.*?))*}}', re.DOTALL)

RE_TR_TAG = re.compile('{{(.*?)}}', re.DOTALL)
TR_TAG_SEP = '|'

def tr_tag_test_matching(s):
    # if s.count('{{') > s.count('}}'): raise
    S = []
    i = 0
    line = 1
    while i < len(s) - 2:
        if s[i] == s[i+1] == '{':
            i += 2
            S.append(line)
        if s[i] == s[i+1] == '}':
            i += 2
            try:
                S.pop()
            except:
                pass # warning(f'early closed at line {line}')
        else:
            if s[i] == '\n':
                line += 1
            i += 1
    if S:
        raise ValueError(f'opening not closed: {S}')

def spliti(s, sep, i, default=None):
    try:
        return s.split(sep)[i]
    except IndexError:
        return default
    # this alg may be faster... but probably not
    k = 0
    pn = 0
    for n in range(len(s)):
        if s[n] == sep:
            if k == i:
                return s[pn:n]
            else:             
                k += 1
                pn = n + 1
    return s[pn:] if k == i else default

modified = []

for f in filter(RE.match, os.listdir('.')):
    if f == 'generate_multilang.py':
        continue
    if args.print_only:
        print(f)
        continue
    fileinfo = fileinfos.get(f, {})
        
    basename, multilang_symbol, othernames, ending = RE.match(f).groups()
    othernames = re.split('\\||_as_', othernames) if othernames else []
    
    with open(f) as fo:
        s = fo.read()
    
    try:
        tr_tag_test_matching(s)
    except ValueError as e:
        warning('In {}: Translation tag not matching: {}'.format(f, str(e)))
        continue
    
    for i, lang in enumerate(fileinfo.get('langs', LANGS)):
        has_other_name = i-1 in range(len(othernames))
        has_info_name = 'name' in fileinfo and lang in fileinfo['name']
        simple_name = basename + multilang_symbol + lang + ending
        filename = (othernames[i-1] + ending if has_other_name else
                    fileinfo['name'][lang] if has_info_name else
                    simple_name)
        
        if os.path.isfile(filename):
            with open(filename, 'r') as fo:
                prev_str = fo.read()
        else:
            prev_str = ''
        
        next_str = RE_TR_TAG.sub(lambda m: spliti(m.group(1), TR_TAG_SEP, i, 'NOT TRANSLATED'), s)
        # ornone = lambda x, y: y if x is None else x
        # next_str = RE_TR.sub(lambda m: ornone(m.group(i+1), m.group(1)), s)
        if prev_str != next_str:
            modified.append(filename)
                
            with OutFile(filename) as fo:
                fo.write(next_str)
            
            if i == 0:
                new = OutFile(basename + ending)
                new.unlock()
                shutil.copy(filename, new.filename)
                new.lock()
                info('Copy', filename, '->', '(read only)', new.filename)
                del new
            
            # TODO: redirects/symlink
            # in: trucs.multilang_as_stuffs.txt
            # trucs.en.txt -> stuff.txt
            # stuff.fr.txt -> trucs.txt
            # trucs.fr.txt -> trucs.txt
            # stuff.en.txt -> stuff.txt
            # if clash: # article.multilang.txt
            #    article.fr.txt is a file, article.txt -> article.fr.txt
            # wikipedia like: stuff fr: 404 stuff en: 200
            # adding "no lang = fr" then "en"
            
            if filename != simple_name:
                try:
                    new = OutFile(simple_name)
                    new.unlock()
                    shutil.copy(filename, simple_name)
                    new.lock()
                    print('Copy', filename, '->', '(read only)', simple_name)
                    del new
                except ValueError:
                    print('simple_name exists and is writable')

print('multilang:', len(modified), 'file' + 's' * (len(modified) != 1) + ' modified' + ':' * bool(modified), ' '.join(modified))
