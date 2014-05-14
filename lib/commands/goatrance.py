#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Goatrance(Base_Command.Base_Command):

    def goatrance(self):
        db = Database()
        self.goatrance = None
        try:
            self.goatrance = db.select('goatrance', 'goatrance', 1)[0][0]
        except:
            return False
        if self.goatrance:
            self.parent.conn.privmsg(self.channel, self.goatrance)

    def run(self):
        self.goatrance()
