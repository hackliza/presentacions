#!/usr/bin/env python3

## References:
## - https://book.hacktricks.xyz/pentesting-web/deserialization/python-yaml-deserialization

import yaml
from yaml import UnsafeLoader, FullLoader, Loader, SafeLoader, CLoader
import sys


with open(sys.argv[1]) as fi:
    data = fi.read()


print("=== Loader=CLoader ===")
yaml.load(data, Loader=CLoader)
print()

try:
    print("=== Loader=FullLoader ===")
    yaml.load(data, Loader=FullLoader)
except Exception as e:
    print("Error: {}\n".format(e))
    
print("=== Loader=Loader ===")
yaml.load(data, Loader=Loader)
print()

try:
    print("=== Loader=SafeLoader ===")
    yaml.load(data, Loader=SafeLoader)
except Exception as e:
    print("Error: {}\n".format(e))

print("=== Loader=UnsafeLoader ===")
yaml.load(data, Loader=UnsafeLoader)
print()

try:
    print("=== safe_load ===")
    yaml.safe_load(data)
except Exception as e:
    print("Error: {}\n".format(e))

print("=== unsafe_load ===")
yaml.unsafe_load(data)
print()
