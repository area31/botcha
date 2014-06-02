#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Rock(Base_Command.Base_Command):

    def rock(self):
        db = Database()
        self.rock = None
        try:
            self.rock = db.select('rock', 'rock', 1)[0][0]
        except:
            return False
        if self.rock:
            self.parent.conn.privmsg(self.channel, self.rock)

    def run(self):
        self.rock()
