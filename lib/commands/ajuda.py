#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command

class Ajuda(Base_Command.Base_Command):

    def ajuda(self):
        self.parent.conn.privmsg(self.channel, '%s' % ('-- comandos disponiveis --'))
        self.parent.conn.privmsg(self.channel, '%s' % ('!ajuda'))
        self.parent.conn.privmsg(self.channel, '%s' % ('!chuck'))
        self.parent.conn.privmsg(self.channel, '%s' % ('!goatrance (!add goatrance)'))
        self.parent.conn.privmsg(self.channel, '%s' % ('!mulher (!add mulher)'))
        self.parent.conn.privmsg(self.channel, '%s' % ('!quote (!add quote)'))
        self.parent.conn.privmsg(self.channel, '%s' % ('!transito'))
        self.parent.conn.privmsg(self.channel, '%s' % ('!xinga (!add xingamento)'))


    def run(self):
        self.ajuda()
