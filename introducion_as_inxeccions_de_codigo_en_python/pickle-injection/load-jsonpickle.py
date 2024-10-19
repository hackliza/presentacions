
import jsonpickle
import sys

with open(sys.argv[1], "r") as fi:
    jsonpickle.loads(fi.read())
