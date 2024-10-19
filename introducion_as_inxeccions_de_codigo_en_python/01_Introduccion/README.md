# Introducción

Nesta charla explicaremos que son as inxeccións de código e como explotalas en Python.

## Que é unha inxección de código?

Unha inxección de código é un tipo de ataque no que se pretende introducir código unha aplicación para que se execúte ou
interprete.

## Por que se produce unha inxección de código?

Este tipo de ataques prodúcense porque non se validan os datos de entrada dos usuarios.

## Onde se produce unha inxección de código?

As inxeccións de código prodúcense en funcións capaces de executár calquera tipo código. En Python esas funcións poden 
ser `eval()` ou `exec()`.

## Quen produce unha inxección de código?

Este tipo de ataques son producidos por atacantes que pretende tomar o control do computador no que se está a executar a
aplicación vulnerable.

## Exemplo

No seguinte exemplo mostrarase un código vulnerable e se pode aproveitar para inxectar código.

### Explicación do código

```python
def main():
    conta = input("Calculadora: ")
    resultado = eval(conta)
    print(resultado)


if __name__ == "__main__":
    main()
```

A liña `conta = input("Calculadora: ")` recolle o input do usuario e gardao na variable conta.

Despois, na liña `resultado = eval(conta)` a función `eval()` executa o se introduciu navariable `conta` e o resultado
gárdase na variable `resultado`.

Finalmente, móstrase na liña `print(resultado)` o resultado da función `eval()` mediante un `print`.

### Execución normal

Unha posible execución sería:

```
Calculadora: 1+1
2
```

Neste caso evalúase unha suma (1+1) e móstrase o resultado (2).

### Execución con inxección de código

Para este caso concreto, como non se fai ningunha comprobación dos datos que se recollen coa función `input()`, pódese
introducir código python directamente para que se execute na función `eval()`.

```
Calculadora: print('Ola!')
Ola!
None
```

Neste caso introducíuse o string `print('Ola!')` o cal execútase na función `eval()` producindo que mostre pola consola 
o string "Ola!".
