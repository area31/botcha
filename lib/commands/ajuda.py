#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command

class Ajuda(Base_Command.Base_Command):

    def ajuda(self):
	if len(self.args) < 1:
		self.parent.conn.privmsg(self.channel, '%s' % ('-- comandos disponiveis --'))
		self.parent.conn.privmsg(self.channel, '%s' % ('!ajuda'))
		self.parent.conn.privmsg(self.channel, '%s' % ('!add'))
		self.parent.conn.privmsg(self.channel, '%s' % ('!chuck'))
		self.parent.conn.privmsg(self.channel, '%s' % ('!goatrance'))
		self.parent.conn.privmsg(self.channel, '%s' % ('!mulher'))
		self.parent.conn.privmsg(self.channel, '%s' % ('!quote'))
		self.parent.conn.privmsg(self.channel, '%s' % ('!transito'))
		self.parent.conn.privmsg(self.channel, '%s' % ('!xinga'))
	else:
			if self.args[0] == 'ajuda':
				self.parent.conn.privmsg(self.channel, '%s' % ('!ajuda nao possui parametros'))				
			if self.args[0] == 'chuck':
				self.parent.conn.privmsg(self.channel, '%s' % ('!chuck nao possui parametros'))
			if self.args[0] == 'goatrance':
				self.parent.conn.privmsg(self.channel, '%s' % ('!goatrance nao possui parametros'))
			if self.args[0] == 'mulher':
				self.parent.conn.privmsg(self.channel, '%s' % ('!mulher nao possui parametros'))
			if self.args[0] == 'quote':
				self.parent.conn.privmsg(self.channel, '%s' % ('!quote nao possui parametros'))
			if self.args[0] == 'transito':
				self.parent.conn.privmsg(self.channel, '%s' % ('!transito nao possui parametros'))
			if self.args[0] == 'xinga':
				self.parent.conn.privmsg(self.channel, '%s' % ('!xinga nickname'))
			if self.args[0] == 'add':
				if len(self.args) > 1:
					if self.args[1] == 'goatrance':
						self.parent.conn.privmsg(self.channel, '%s' % ('!add goatrance url'))
					if self.args[1] == 'mulher':
						self.parent.conn.privmsg(self.channel, '%s' % ('!add mulher link da mulher'))
					if self.args[1] == 'quote':
						self.parent.conn.privmsg(self.channel, '%s' % ('!add quote frase'))
					if self.args[1] == 'goatrance':
						self.parent.conn.privmsg(self.channel, '%s' % ('!add xinga frase'))
		


    def run(self):
        self.ajuda()
