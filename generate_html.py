#!/usr/bin/env python3
import os, re
import textwrap
try:
    import html
except ImportError:
    import cgi as html
    
def django_format(template, **args):
    ''' Difference with django : arguments are SAFE '''
    return re.sub(r'\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}', lambda m: '{}'.format(args.get(m.group(1), '')), template)

from generate_ls import GROUPINGS

if __name__ == '__main__':
    RE0 = re.compile('.*\.(py|php|java)$')
    REE = re.compile('.*\.(.*)$')
    RE = re.compile('({})(\d+)'.format('|'.join(map(re.escape, GROUPINGS))))

    import itertools
    it = itertools.count(1000)
    all_grouped = {
        typename: {
            (
                int(RE.match(f).group(2) if RE.match(f) else next(it)),
                (REE.match(f).group(1) if REE.match(f) else '')
            ):f
            for f in os.listdir('.')
            if RE0.match(f) and not os.path.islink(f)
            if f.startswith(typename)
        }
        for typename in GROUPINGS
    } # {theorie: {(1, py):theorie1_begin.py}}
        
    with open('template_codefile.html') as f:
        TEMPLATE = f.read()
    
    modifs = []
    for f in os.listdir('.'):
        m0 = RE0.match(f)
        if m0:
            pdf_name = "pdf_{}.pdf".format(f)
            m = RE.match(f)
            if m:
                typename, num = (m.group(1), int(m.group(2)))
                t = (REE.match(f).group(1) if REE.match(f) else '')
                
            with open(f) as fi:
                res = django_format(
                    TEMPLATE, 
                    code=html.escape(fi.read(), quote=False),
                    codelang = m0.group(1),
                    name=f,
                    postnav='' if not os.path.isfile(pdf_name) else '''
                        <a href="{}">#pdf</a>
                    '''.format(pdf_name),
                    nav='' if not m else '''
                        <a class="keephash" href="{url_prev}"><img style="width:24px; height:24px; vertical-align: middle;" src="prev.png"/></a>
                        <a class="keephash" href="{url_next}"><img style="width:24px; height:24px; vertical-align: middle;" src="next.png"/></a>
                        <a class="keephash" href="{url_next}">#{name}</a>
                    '''.format(
                        name=f,
                        type=typename,
                        url_prev = '{base}.html'.format(base=all_grouped[typename].get((num-1,t), 'index.html')),
                        url_next = '{base}.html'.format(base=all_grouped[typename].get((num+1,t), 'index.html')),
                    )
                )
                try:
                    with open(f + '.html', 'r') as fl:
                        before = fl.read()
                except:
                    before = ''
                if res != before:
                    modifs.append(f)
                    with open(f + '.html', 'w') as fl:
                        fl.write(res)
                        
    print("No files modified" if not modifs else "Files modified : ({}) {}".format(len(modifs), ' '.join(modifs)))