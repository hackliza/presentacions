
import pickle
import sys

class Person():

    def __init__(self, name):
        self.name = name
        if name == "isabel":
            self.category = "queen"
        else:
            self.category = "servant"
        self.file = open("/tmp/a.txt", "w")

    def __reduce__(self):
        return self.__class__, ("ada",) 

with open(sys.argv[1], "rb") as fi:
    print(pickle.load(fi))

