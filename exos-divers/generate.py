#!/usr/bin/env python3
"""
Creates index.html from os.listdir('.')
"""
import argparse
p = parser = argparse.ArgumentParser()
a = args = parser.parse_args()

import os

def modified(filename) -> str:
    import os; from datetime import datetime, date
    return str(date.fromtimestamp(os.stat(filename).st_mtime))

def toletter(i:'int[range(26)]') -> 'str[length=1]':
    if i not in range(26):
        raise Exception()
    return chr(ord('A') + i)

from functools import partial
enumerate1 = partial(enumerate, start=1)

from itertools import filterfalse

with open('index.html', 'w') as w:
    l = sorted(os.listdir('.'), key=modified)
    w.write('<pre style="font-family:serif">\n' + 
'''\
{nd} dirs
{list_dir}

{nf} files
{list_files}
'''.format(
nd=len(list(filter(os.path.isdir, l))),
nf=len(list(filterfalse(os.path.isdir, l))),
list_dir='\n'.join(f'''\
- {modified}: <a href="{name}">{name}</a>  \
''' for i, name, modified in [(toletter(i), name, modified(name)) for i,name in enumerate(l for l in l if os.path.isdir(l))]),
list_files='\n'.join(f'''\
- {modified}: <a href="{name}">{name}</a>  \
''' for i, name, modified in [(toletter(i), name, modified(name)) for i,name in enumerate(l for l in l if not os.path.isdir(l))])))
