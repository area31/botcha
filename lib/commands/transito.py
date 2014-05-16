#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.web import Web

class Transito(Base_Command.Base_Command):

    def transito(self):
        web = Web()
        answerSP = web.html(web.get('http://cetsp1.cetsp.com.br/monitransmapa/agora/'))
        if answerSP:
            dados = {
                'hora': answerSP.find('div', id="hora").findAll(text=True)[0],
                'lentidao': answerSP.find('div', id="lentidao").findAll(text=True)[0],
            }
            result = "%(lentidao)s km de transito em SP, atualizado as %(hora)s" % dados
	    self.parent.conn.privmsg(self.channel, result)
        else:
            return False


    def run(self):
        self.transito()
