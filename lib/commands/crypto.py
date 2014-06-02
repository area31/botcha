#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Crypto(Base_Command.Base_Command):

    def crypto(self):
        if len(self.args) < 1:
	    var_crypt = open("/home/morfetico/botcha/crypt-current.txt")
	    var_senha = var_crypt.read()
	    self.parent.conn.privmsg(self.nick, 'a senha é:    ' + var_senha)
            self.parent.conn.privmsg(self.channel,'%s, Te enviei a senha do dia via PVT ;) Qualquer dúvida RTFM --> http://www.area31.net.br/wiki/IRC#Criptografe_suas_conversas_no_canal' % self.nick)
    def run(self):
        self.crypto()
