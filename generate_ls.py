#!/usr/bin/env python3
from __future__ import print_function

import os, re
from functools import partial
import textwrap

from generate_utils import OutFileGreen as OutFile

from generate_info import GROUPINGS, EXTS, TRANSLATION_INFO

def get_group_i(name):
    return next(i for i,n in enumerate(GROUPINGS) if name.startswith(n))
    # return next(i for i,n in enumerate(re.match('(theorie)|(exercice)|(math)|(pythontutor)|()', name).groups()) if n is not None)
    
def key(path):
    name = os.path.basename(path)
    ext = os.path.splitext(path)[1]
    return (not os.path.isdir(path), get_group_i(name), EXTS.get(ext, 1000), ext, name)

_GENERATED_FILES = {
    translated_filename
    for f, langs in TRANSLATION_INFO.items()
    for lang, translated_filename in langs.items()
}

def accepted(path):
    name = os.path.basename(path)
    if name in TRANSLATION_INFO:
        return False
    if name in _GENERATED_FILES:
        pass # if currentlang == document.lang: pass else: return False
    return not any(
        re.search(m, name)
        for m in (
            '^\\.', '^__pycache__$', '^private$', '^presences$',
            '\\.py\\.txt$', '\\.pyc$', '\\.py\\.html$',
            '\\.en\\.html$', '\\.fr\\.html$', '[._]multilang\\.html$',
            '\\.php\\.txt$', '\\.php\\.html$',
            '\\.java\\.txt$', '\\.class$', '\\.java\\.html$',
            '\\.js\\.txt$', '\\.js\\.html$', '^home$'
        )
    ) and not os.path.islink(path)

lastgroup = len(GROUPINGS) - 1
def content(path, indent=0):
    """
    hello/world.txt -> <a href="hello/world.txt">world.txt</a>
    hello (dir) -> hello <ul> <li>{}</li> ... <li>{}</li> </ul>
    hello.py -> html for: hello.py [txt] [py]
    """
    global lastgroup
    g = get_group_i(os.path.basename(path))
    changegroup = g != lastgroup
    lastgroup = g
    
    RE0 = re.compile('.*(py|php|java|js)$')
    REE = re.compile('.*\\.(.*)$')
    
    if not os.path.isdir(path):
        return (
            '</section>' if changegroup and lastgroup != -1 else ''
        ) + (
            '<section class="grouping" id="{}"/>'.format(GROUPINGS[g]) if changegroup else ''
        ) + (
            "<li class='ext-{2}'><a href='{0}'>{1}</a></li>" if not RE0.match(path) else
            # <a href='{0}.txt'>[txt]</a> <a href='{0}'>[py]</a> 
            "<li class='ext-{2}'><a href='{0}.html'>{1}</a></li>"
        ).format(path, os.path.basename(path), (REE.match(path).group(1) if REE.match(path) else ''))
    else:
        return ('<span class="notitle dir-name {cls}">{name}</span>\n{ind}{ulbeg}\n{sub}\n{ind}{ulend}').format(
            ulbeg = '<ul>' if path != '.' else '',
            ulend = '</ul>' if path != '.' else '',
            cls = 'root' if path == '.' else '',
            ind = indent * '    ',
            name = os.path.basename(path) if not RE0.match(path) else os.path.basename(path[:-3]),
            sub = '\n'.join(
                map(((1 + indent) * '    ' + '{}').format,
                map(partial(content, indent=indent+1),
                filter(accepted,
                map(partial(os.path.join, path),
                partial(sorted, key=key)(os.listdir(path))))))
            )
        )
if __name__ == '__main__':
    with open('template.html') as f:
        template = f.read()

    with open('plan.svg') as f:
        plan_svg_content = f.read()
        
    with OutFile('index.html') as f:
        f.write(template
                .replace('{% include "plan.svg" %}', plan_svg_content)
                .replace('{{ list }}', content('.', indent=3) + '</section>'))
