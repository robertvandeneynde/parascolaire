#!/usr/bin/env python3
import os, re
from functools import partial
import textwrap

for f in os.listdir('.'):
    if not os.path.islink(f):
        m = re.match('(theorie|exercice)(\d+).*(\\.py(\\.html|\\.txt)?)$', f)
        if m:
            os.system('ln -sf "{f}" {zero}{one}{two}'.format(f=f, zero=m.group(1), one=m.group(2), two=m.group(3)))