#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Ama(Base_Command.Base_Command):

    def ama(self):
        if len(self.args) < 1:
            self.parent.conn.privmsg(self.channel,'%s, deixa de ser burro e ama alguém. ' % self.nick)	
        else:
            db = Database()
            self.ama = None
            try:
                self.ama = db.select('ama', 'amoroso', 1)[0][0]
            except:
                return False
            if self.ama:
                self.parent.conn.privmsg(self.channel, '%s, %s' % (self.args[0], self.ama))

    def run(self):
        self.ama()
