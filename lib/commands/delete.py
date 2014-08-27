#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Delete(Base_Command.Base_Command):

    def admin(self, _nick):
        db = Database()
        try:
            db.delete('admins', 'admin', _nick.strip())
        except:
            return False
        return True

    def delete(self):
        if len(self.args) > 1:
            content = ' '.join(self.args[1:])
            result = None
            if self.args[0] == 'admin' and self.check_admin():
                result = self.admin(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, %s removido." % (self.nick, self.args[0]))

    def run(self):
        self.delete()
