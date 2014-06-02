#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Zuera(Base_Command.Base_Command):

    def zuera(self):
        db = Database()
        self.zuera = None
        try:
            self.zuera = db.select('zuera', 'zuera', 1)[0][0]
        except:
            return False
        if self.zuera:
            self.parent.conn.privmsg(self.channel, self.zuera)

    def run(self):
        self.zuera()
