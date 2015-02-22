#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Nerdices(Base_Command.Base_Command):

    def nerdices(self):
        db = Database()
        self.nerdices = None
        try:
            self.nerdices = db.select('nerdices', 'nerdices', 1)[0][0]
        except:
            return False
        if self.nerdices:
            self.parent.conn.privmsg(self.channel, self.nerdices)

    def run(self):
        self.nerdices()
