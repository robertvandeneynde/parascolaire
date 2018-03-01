#!/usr/bin/env python3
from __future__ import print_function

import os, re, shutil, json
import argparse

from generate_utils import OutFile

p = argparse.ArgumentParser()
p.add_argument('--files', nargs='*', help='to implement') # TODO to implement
p.add_argument('-l', '--langs', nargs='+')
p.add_argument('--config', nargs='?', default={})
p.add_argument('--print-only', action="store_true", help="doesn't create file, only print file concerned")
a = args = p.parse_args()

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
RE_TR = re.compile('{{(.*?)\|(.*?)}}', re.DOTALL)

modified = []

def is_user_writable(filepath):
  import os, stat
  return bool(os.stat(filepath).st_mode & stat.S_IWUSR)

for f in filter(RE.match, os.listdir('.')):
    if f == 'generate_multilang.py':
        continue
    if args.print_only:
        print(f)
        continue
    fileinfo = fileinfos.get(f, {})
        
    basename, multilang_symbol, othernames, ending = RE.match(f).groups()
    othernames = re.split('\\||_as_', othernames) if othernames else []
    with open(f) as f:
        s = f.read()
    
    for i, lang in enumerate(fileinfo.get('langs', LANGS)):
        has_other_name = i-1 in range(len(othernames))
        has_info_name = 'name' in fileinfo and lang in fileinfo['name']
        simple_name = basename + multilang_symbol + lang + ending
        filename = (othernames[i-1] + ending if has_other_name else
                    fileinfo['name'][lang] if has_info_name else
                    simple_name)
        
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                prev_str = f.read()
        else:
            prev_str = ''
        
        next_str = RE_TR.sub(lambda m: m.group(i+1), s)
        if prev_str != next_str:
            modified.append(filename)
                
            with OutFile(filename) as f:
                f.write(next_str)
            
            if i == 0:
                new = OutFile(basename + ending)
                new.unlock()
                shutil.copy(filename, new.filename)
                new.lock()
                print('Copy', filename, '->', '(read only)', new.filename)
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
