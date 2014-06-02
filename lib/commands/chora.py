#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Chora(Base_Command.Base_Command):

    def chora(self):
        if len(self.args) < 1:
            self.parent.conn.privmsg(self.channel,'%s, deixa de ser burro e deprime alguem direito. ' % self.nick)	
        else:
            db = Database()
            self.chora = None
            try:
                self.chora = db.select('chora', 'chora', 1)[0][0]
            except:
                return False
            if self.chora:
                self.parent.conn.privmsg(self.channel, '%s, %s' % (self.args[0], self.chora))

    def run(self):
        self.chora()
