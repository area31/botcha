#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command

class Ajuda(Base_Command.Base_Command):

    def ajuda(self):
	if len(self.args) < 1:
		self.parent.conn.privmsg(self.channel, '%s' % ('-- comandos disponiveis --'))
		self.parent.conn.privmsg(self.channel, '%s' % ('!add  |  !ajuda  |  !ama  |  !btc  |  !chill  |  !chora  |  !chuck  |  !cotacao  |  !crypto  |  !docs  |  !goatrance  |  !imdb  |  !ipinfo  |  !mulher  |  !noob  |  !politica  |  !quote  |  !rock  |  !transito  |  !weather  |  !xinga  |  !zuera  '))
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
			if self.args[0] == 'ama':
				self.parent.conn.privmsg(self.channel, '%s' % ('!ama nickname'))
			if self.args[0] == 'docs':
				self.parent.conn.privmsg(self.channel, '%s' % ('!docs nao possui parametros'))
			if self.args[0] == 'add':
				if len(self.args) > 1:
					if self.args[1] == 'goatrance':
						self.parent.conn.privmsg(self.channel, '%s' % ('!add goatrance url'))
					if self.args[1] == 'mulher':
						self.parent.conn.privmsg(self.channel, '%s' % ('!add mulher link da gostosa'))
					if self.args[1] == 'quote':
						self.parent.conn.privmsg(self.channel, '%s' % ('!add quote frase'))
					if self.args[1] == 'xinga':
						self.parent.conn.privmsg(self.channel, '%s' % ('!add xingamento frase ofensiva'))
					if self.args[1] == 'ama':
						self.parent.conn.privmsg(self.channel, '%s' % ('!add xinga frase amorosa'))
					if self.args[1] == 'docs':
						self.parent.conn.privmsg(self.channel, '%s' % ('!add docs link de artigo'))
				else:
					self.parent.conn.privmsg(self.channel, '%s' % ('-- ajudas disponiveis --'))
					self.parent.conn.privmsg(self.channel, '%s' % ('!ajuda add goatrance'))
					self.parent.conn.privmsg(self.channel, '%s' % ('!ajuda add mulher'))
					self.parent.conn.privmsg(self.channel, '%s' % ('!ajuda add quote'))
					self.parent.conn.privmsg(self.channel, '%s' % ('!ajuda add xingamento'))
					self.parent.conn.privmsg(self.channel, '%s' % ('!ajuda add ama'))
					self.parent.conn.privmsg(self.channel, '%s' % ('!ajuda add docs'))
		


    def run(self):
        self.ajuda()
