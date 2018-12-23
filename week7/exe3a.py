#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import yaml
from pprint import pprint

filename = 'exe3a.yml'
with open(filename) as f:
    output = yaml.load(f)

print()
pprint(output)
print()
