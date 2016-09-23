#!/usr/bin/env python3
import os, re
from functools import partial
import textwrap

for f in os.listdir('.'):
    if os.path.islink(f) or f.endswith('.py.html') or f.endswith('.py.txt'):
        os.remove(f)
