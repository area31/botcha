#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.web import Web

class Dicionario(Base_Command.Base_Command):

    def dic(self):
	if len(self.args) < 1:
		self.parent.conn.privmsg(self.channel, '%s' % ('Digite a palavra que gostaria de procurar'))
	else:
		web = Web()
		answer = web.html(web.get('http://michaelis.uol.com.br/moderno/portugues/index.php?lingua=portugues-portugues&palavra='+self.args[0]))
		if answer:
			dados = {
				'significado': answer.find('div', id="descricao").findAll(text=True)[0],
			}
			result = "Significado: %(significado)s " % dados
			self.parent.conn.privmsg(self.channel, result)
		else:
		    return False

    def run(self):
        self.transito()