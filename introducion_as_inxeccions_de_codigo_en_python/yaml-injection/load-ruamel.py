#!/usr/bin/env python3
from ruamel.yaml import YAML
import sys

with open(sys.argv[1]) as fi:
    data = fi.read()

try:
    print("=== Using YAML() ===")
    print(YAML().load(data))
except Exception as e:
    print("Error: {}\n".format(e))
    
try:
    print("=== Using YAML(typ='safe') ===")
    print(YAML(typ="safe").load(data))
except Exception as e:
    print("Error: {}\n".format(e))
    
try:
    print("=== Using YAML(typ='unsafe') ===")
    print(YAML(typ="unsafe").load(data))
except Exception as e:
    print("Error: {}\n".format(e))
