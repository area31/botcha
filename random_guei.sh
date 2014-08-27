#!/bin/bash

GUEI_SORTEADO=$(shuf -n 1 /home/morfetico/botcha/listas/random_guei_list.txt)

cp /home/morfetico/botcha/lib/commands/guei.py.template /home/morfetico/botcha/lib/commands/guei.py

sed -i s,{TEMPORARY_USER},${GUEI_SORTEADO},g /home/morfetico/botcha/lib/commands/guei.py
