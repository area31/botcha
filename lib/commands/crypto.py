#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Crypto(Base_Command.Base_Command):

    def crypto(self):
        if self.check_admin():
            db = Database()
            try:
                _hash = db.select('hash', 'crypto')[0][0]
	        self.parent.conn.privmsg(self.nick, '######################################################################')
	        self.parent.conn.privmsg(self.nick, 'Remova a senha antiga:    /delkey #area31')
	        self.parent.conn.privmsg(self.nick, 'Adicione a nova senha (de dentro do #area31):    /setkey ' + _hash)
                self.parent.conn.privmsg(self.channel,'%s, Te enviei a senha do dia via PVT. Dicas, digite: !ajuda crypto     [ Qualquer dúvida RTFM --> http://a31.com.br/crypto-irc ]' % self.nick)
            except:
                return False
    def run(self):
        self.crypto()
