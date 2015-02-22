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
                self.parent.conn.privmsg(self.channel,'%s, Te enviei a senha do dia via PVT. Dicas, digite: !ajuda crypto     [ Qualquer dúvida RTFM --> http://a31.com.br/crypto-irc ]' % self.nick)
	        self.parent.conn.privmsg(self.nick, ' ')
	        self.parent.conn.privmsg(self.nick, ' ')
	        self.parent.conn.privmsg(self.nick, '%%%  CHAVE CRIPTOGRAFICA DO DIA %%%')
	        self.parent.conn.privmsg(self.nick, '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
	        self.parent.conn.privmsg(self.nick, 'Adicione a nova senha (irssi):         /blowkey #area31 cbc:' + _hash)
	        self.parent.conn.privmsg(self.nick, '#######################################################')
	        self.parent.conn.privmsg(self.nick, 'Remova a senha antiga (XCHAT):         /delkey #area31')
	        self.parent.conn.privmsg(self.nick, 'Adicione a nova senha (XCHAT):         /setkey #area31 ' + _hash)
	        self.parent.conn.privmsg(self.nick, '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
	        self.parent.conn.privmsg(self.nick, '%%%  Area31 Hackerspace - Lembre-se de de NUNCA digitar esses comandos no canal irc  %%%')
            except:
                return False
    def run(self):
        self.crypto()
