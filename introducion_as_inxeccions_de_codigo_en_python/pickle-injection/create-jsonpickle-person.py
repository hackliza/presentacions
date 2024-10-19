import jsonpickle

class Person():

    def __init__(self, name):
        self.name = name

def main():
    output_file = "person.pickle.json"
    with open(output_file, "w") as fo:
        fo.write(jsonpickle.dumps(Person("ada")))

    print("Saved in {}".format(output_file))

if __name__ == "__main__":
    exit(main())
