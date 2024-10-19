class Sandbox:
    def __init__(self, globals=None, locals=None):
        self.globals = globals
        self.locals = locals

    def evalua(self, codigo):
        resultado = eval(codigo, self.globals, self.locals)
        print(resultado)


def main():
    sandbox = Sandbox()
    codigo = input("Codigo: ")
    sandbox.evalua(codigo)


if __name__ == "__main__":
    main()
