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

def format_list_ls_style(li, W=100, FW=None):
    li = list(map("{}".format, li))
    '''
    Demo:
    for i in range(0,70,5):
        print(i * '-')
        print(format_list_ls_style(['hello', 'world', 'how', 'is', 'life', 'yo', 'wadup', 'I have'], i))
    '''
    if FW is None: FW = W
    # assert FW <= W
    
    if sum(map(len,li)) + len(li) < FW:
        return ' '.join(li)
    
    M = 1 + max(list(map(len,li)))
    if M > W:
        return '\n'.join(li)
    
    C = W // M # number of columns
    it = iter(li)
    lines = []
    while True:
        lines.append(
            ''.join(
                ("{:%d}" % M).format(x)
                for y,x in zip(list(range(C)), it)
            )
        )
        if lines[-1] == '':
            del lines[-1]
            break
    return '\n'.join(lines)

from generate_ls import GROUPINGS

if __name__ == '__main__':
    RE0 = re.compile('.*\.(py|php|java|js)$')
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
                        url_prev = '{}.html'.format(all_grouped[typename].get((num-1,t), 'index')),
                        url_next = '{}.html'.format(all_grouped[typename].get((num+1,t), 'index')),
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
    print('generate_html:', len(modifs), 'file' + 's' * (len(modifs) != 1) + ' modified' + ':' * bool(modifs), ' '.join(modifs))