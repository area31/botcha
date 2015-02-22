#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Reggae(Base_Command.Base_Command):

    def reggae(self):
        db = Database()
        self.reggae = None
        try:
            self.reggae = db.select('reggae', 'reggae', 1)[0][0]
        except:
            return False
        if self.reggae:
            self.parent.conn.privmsg(self.channel, self.reggae)

    def run(self):
        self.reggae()
