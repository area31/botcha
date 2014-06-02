#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Politica(Base_Command.Base_Command):

    def politica(self):
        db = Database()
        self.politica = None
        try:
            self.politica = db.select('politica', 'politica', 1)[0][0]
        except:
            return False
        if self.politica:
            self.parent.conn.privmsg(self.channel, self.politica)

    def run(self):
        self.politica()
