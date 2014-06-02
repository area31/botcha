#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Noob(Base_Command.Base_Command):

    def noob(self):
        if len(self.args) < 1:
            self.parent.conn.privmsg(self.channel,'%s, deixa de ser burro e noob alguém. ' % self.nick)	
        else:
            db = Database()
            self.noob = None
            try:
                self.noob = db.select('noob', 'noob', 1)[0][0]
            except:
                return False
            if self.noob:
                self.parent.conn.privmsg(self.channel, '%s, %s' % (self.args[0], self.noob))

    def run(self):
        self.noob()
