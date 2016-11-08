#!/usr/bin/env python3
import os, shutil, re

RE0 = re.compile('.*\\.(py|php|java|js)$')

for f in os.listdir('.'):
    if RE0.match(f):
        shutil.copy(f, f + '.txt')
