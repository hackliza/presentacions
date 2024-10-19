class Sandbox:
    def __init__(self, globals=None, locals=None):
        self.globals = globals
        self.locals = locals

    def evalua(self, codigo):
        exec(codigo, self.globals, self.locals)


def main():
    sandbox = Sandbox()
    codigo = input("Codigo: ")
    if "subprocess" in codigo:
        print("Detectado intento de inxeccion de código")
        exit(0)
    sandbox.evalua(codigo)


if __name__ == "__main__":
    main()
