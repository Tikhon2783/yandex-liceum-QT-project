import sqlite3
from hashlib import sha256

class Database():
    def __init__(self, filepath):
        try:
          self.conn = sqlite3.connect(filepath)
          self.cur = self.conn.cursor()
        except Exception as err:
          raise Exception('Error trying to connecto to a database:', err)
    
    def register_user(self, username, password):
       psw_hash = sha256(password.encode()).hexdigest()
       self.cur.execute('''INSERT INTO users(username, password) VALUES(?, ?)''', (username, psw_hash))
       self.cur.execute('''INSERT INTO records(username, wins) VALUES(?, 0)''', (username,))
       self.conn.commit()
    
    def check_user(self, username, password):
       stored_hash = self.cur.execute('''SELECT password FROM users WHERE username = ?''', (username,)).fetchall()
       psw_hash = sha256(password.encode()).hexdigest()
       return psw_hash == stored_hash[0][0]
    
    def add_win(self, username):
       self.cur.execute('''UPDATE records SET wins = (SELECT wins FROM records WHERE username = ?) + 1 WHERE username = ?''',
                        (username, username))
       self.conn.commit()
    
    def get_lb(self):
       return self.cur.execute('''SELECT * FROM records''')
