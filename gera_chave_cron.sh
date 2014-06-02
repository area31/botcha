#!/bin/bash

# gera chaves do canal IRC #area31
#01 00 * * *     morfetico /home/morfetico/botcha/gera_chave_cron.sh

python /home/morfetico/botcha/gera_chave.py > /home/morfetico/botcha/crypt-current.txt 2> /home/morfetico/botcha/log/gera_chave.log

