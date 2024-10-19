import pickle

class Person():

    def __init__(self, name):
        self.name = name


def main():
    output_file = "person.pickle"
    with open(output_file, "wb") as fo:
        pickle.dump(Person("ada"), fo)

    print("Saved in {}".format(output_file))

if __name__ == "__main__":
    exit(main())
