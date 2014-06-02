#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Chill(Base_Command.Base_Command):

    def chill(self):
        db = Database()
        self.chill = None
        try:
            self.chill = db.select('chill', 'chill', 1)[0][0]
        except:
            return False
        if self.chill:
            self.parent.conn.privmsg(self.channel, self.chill)

    def run(self):
        self.chill()
