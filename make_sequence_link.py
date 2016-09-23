import argparse

parser = argparse.ArgumentParser()
parser.add_argument('section')
parser.add_argument('data')
parser.add_argument('tag', nargs='?', default='h3')

args = lambda : None # parser.parse_args()

args.section = 'forces'
args.data = '''
loi-de-newton        La loi de Newton : F = ma
chute-libre           Chute libre
gravite              Gravité de planètes et attraction de charges
ressort              Ressort
frottement-lineaire  Frottement linéaire
frottement-air       Frottement de l'air
'''
args.tag = 'h3'

D = [
    {'id':a, 'text':b, 'parent':args.section, 'prev':'', 'next': ''}
    for l in args.data.strip().split('\n')
    for x in [l.strip().split()]
    for a,b in [(x[0], ' '.join(x[1:]))]
]

for a,b in zip(D, D[1:]):
    a['next'] = b['id']
    b['prev'] = a['id']

from functools import partial

first = partial(
    '''<{tag} id="{id}"><a href="#{parent}">^</a> <a href="#{parent}" class="prev"></a> <a href="#{next}" class="next"> {text}</a></{tag}>'''.format,
    tag = args.tag
)

middle = partial(
    '''<{tag} id="{id}"><a href="#{parent}">^</a> <a href="#{prev}" class="prev"></a> <a href="#{next}" class="next"> {text}</a></{tag}>'''.format,
    tag = args.tag
)

last = partial(
    '''<{tag} id="{id}"><a href="#{parent}">^</a> <a href="#{prev}" class="prev"></a> <a class="next"> {text}</a></{tag}>'''.format,
    tag = args.tag
)

print('\n'.join([
    first(**D[0])
] + [
    middle(**d) for d in D[1:-1]
] + [
    last(**D[-1])
]))