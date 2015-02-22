#  -*- coding: utf-8 -*-
#

from lib.commands import Base_Command

class Ajuda(Base_Command.Base_Command):

    def ajuda(self):
	if len(self.args) < 1:
                self.parent.conn.privmsg(self.channel,'%s, Te enviei algumas dicas, vamos conversar via PVT.... me pergunte por lá ok? :D' % self.nick)
                self.parent.conn.privmsg(self.nick, ' ')
                self.parent.conn.privmsg(self.nick, ' ')
		self.parent.conn.privmsg(self.nick, '%s' % ('-- comandos disponiveis --'))
		self.parent.conn.privmsg(self.nick, '%s' % ('!add  |  !ajuda  |  !ama  |  !btc  |  !chill  |  !chora  |  !chuck  |  !cotacao  |  !crypto  |  !docs  |  !goatrance  |  !imdb  |  !ipinfo  |  !mulher  |  !nerdices  |  !noob  |  !politica  |  !quote  |  !reggae  |  !rock  |  !transito  |  !weather  |  !xinga  |  !zuera  '))
	else:
                        if self.args[0] == 'ajuda':
                                self.parent.conn.privmsg(self.nick, '%s' % ('!ajuda nao possui parametros'))
                        if self.args[0] == 'chuck':
                                self.parent.conn.privmsg(self.nick, '%s' % ('!chuck nao possui parametros'))
                        if self.args[0] == 'goatrance':
                                self.parent.conn.privmsg(self.nick, '%s' % ('!goatrance nao possui parametros'))
                        if self.args[0] == 'mulher':
                                self.parent.conn.privmsg(self.nick, '%s' % ('!mulher nao possui parametros'))
                        if self.args[0] == 'quote':
                                self.parent.conn.privmsg(self.nick, '%s' % ('!quote nao possui parametros'))
                        if self.args[0] == 'transito':
                                self.parent.conn.privmsg(self.nick, '%s' % ('!transito nao possui parametros'))
                        if self.args[0] == 'xinga':
                                self.parent.conn.privmsg(self.nick, '%s' % ('!xinga nickname'))
                        if self.args[0] == 'ama':
                                self.parent.conn.privmsg(self.nick, '%s' % ('!ama nickname'))
                        if self.args[0] == 'docs':
                                self.parent.conn.privmsg(self.nick, '%s' % ('!docs nao possui parametros'))
                        if self.args[0] == 'add':
                                if len(self.args) > 1:
                                        if self.args[1] == 'goatrance':
                                                self.parent.conn.privmsg(self.nick, '%s' % ('!add goatrance url'))
                                        if self.args[1] == 'mulher':
                                                self.parent.conn.privmsg(self.nick, '%s' % ('!add mulher link da gostosa'))
                                        if self.args[1] == 'quote':
                                                self.parent.conn.privmsg(self.nick, '%s' % ('!add quote frase'))
                                        if self.args[1] == 'xinga':
                                                self.parent.conn.privmsg(self.nick, '%s' % ('!add xingamento frase ofensiva'))
                                        if self.args[1] == 'ama':
                                                self.parent.conn.privmsg(self.nick, '%s' % ('!add xinga frase amorosa'))
                                        if self.args[1] == 'docs':
                                                self.parent.conn.privmsg(self.nick, '%s' % ('!add docs link de artigo'))
                                else:
                                        self.parent.conn.privmsg(self.nick, '%s' % ('-- ajudas disponiveis --'))
                                        self.parent.conn.privmsg(self.nick, '%s' % ('!ajuda add goatrance'))
                                        self.parent.conn.privmsg(self.nick, '%s' % ('!ajuda add mulher'))
                                        self.parent.conn.privmsg(self.nick, '%s' % ('!ajuda add quote'))
                                        self.parent.conn.privmsg(self.nick, '%s' % ('!ajuda add xingamento'))
                                        self.parent.conn.privmsg(self.nick, '%s' % ('!ajuda add ama'))
                                        self.parent.conn.privmsg(self.nick, '%s' % ('!ajuda add docs'))

		
			if self.args[0] == 'crypto':
				if len(self.args) > 1:
					if self.args[1] == 'xchat':
                                                self.parent.conn.privmsg(self.nick, '%s' % ('/setkey senha_do_morfetico   - (Adiciona chave do dia)'))
                                                self.parent.conn.privmsg(self.nick, '%s' % ('/delkey #area31   - (Remove chave do dia)'))
                                                self.parent.conn.privmsg(self.nick, '%s' % ('/encrypt 0   - (Desativa envio criptografado, enviando msgs em plain text no canal)'))
                                                self.parent.conn.privmsg(self.nick, '%s' % ('/encrypt 1   - (Ativa envio criptografado, enviando msgs em criptografadas com a chave do dia no canal)'))

                                        if self.args[1] == 'irssi':
                                                self.parent.conn.privmsg(self.nick, '%s' % ('/blowkey <user|chan> cbc:senha_do_morfetico   - (Adiciona chave do dia)'))
                                                self.parent.conn.privmsg(self.nick, '%s' % ('/blowdel <user|chan>   - (Remove chave do dia)'))
                                                self.parent.conn.privmsg(self.nick, '%s' % ('/blowoff   - (Desativa envio criptografado, enviando msgs em plain text no canal)'))
                                                self.parent.conn.privmsg(self.nick, '%s' % ('/blowon   - (Ativa envio criptografado, enviando msgs em criptografadas com a chave do dia no canal)'))
                                                self.parent.conn.privmsg(self.nick, '%s' % ('/blowkeyx <cbc|ebc> <user|chan>   - (Perform DH1080 key exchange with user)'))
                                else:
                                        self.parent.conn.privmsg(self.nick, '%s' % ('-- Comandos de crypto disponiveis --'))
                                        self.parent.conn.privmsg(self.nick, '%s' % ('!crypto   - (Solicita chave do dia ao BOT)'))
                                        self.parent.conn.privmsg(self.nick, '%s' % ('!ajuda crypto xchat   - (Exibe dicas para o plugin py-fishcrypt para XChat - https://github.com/area31/py-fishcrypt)'))
                                        self.parent.conn.privmsg(self.nick, '%s' % ('!ajuda crypto irssi   - (Exibe dicas para o plugin blowssi para IRSSI - http://linkerror.com/blowssi.cgi)'))

    def run(self):
        self.ajuda()
