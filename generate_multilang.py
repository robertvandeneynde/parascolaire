#!/usr/bin/env python3


import os, re, shutil

RE = re.compile('^(.*)\\.multilang(.[^.]*)$')
RE_TR = re.compile('{{(.*?)\|(.*?)}}', re.DOTALL)

modified = []

for f in filter(RE.match, os.listdir('.')):
    g = RE.match(f).groups()
    with open(f) as f:
        s = f.read()
    for i, lang in enumerate('fr en'.split()):
        filename = g[0] + '.' + lang + g[1]
        
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                prev_str = f.read()
        else:
            prev_str = ''
        
        next_str = RE_TR.sub(lambda m: m.group(i+1), s)
        if prev_str != next_str:
            modified.append(filename)
                
            if os.path.isfile(filename):
                os.chmod(filename, 0o644) # read write
            with open(filename, 'w') as f:
                f.write(next_str)
            os.chmod(filename, 0o444) # read only 
            
            if i == 0:
                if os.path.isfile(g[0] + g[1]):
                    os.chmod(g[0] + g[1], 0o600) # read write
                shutil.copy(filename, g[0] + g[1])
                os.chmod(g[0] + g[1], 0o400) # read only 

print('multilang:', len(modified), 'file' + 's' * (len(modified) != 1) + ' modified' + ':' * bool(modified), ' '.join(modified))
