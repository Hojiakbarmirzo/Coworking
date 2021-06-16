import sqlite3
class DBHelper:
    def __init__(self , db_name):
        self.conn= sqlite3.connect(db_name, check_same_thread=False) 
        self.conn.row_factory=sqlite3.Row
        self.cursor= self.conn.cursor()
    
    def add_info(self, id, phoneNumber, name, surname, group, teacher):
        self.cursor.execute('''INSERT INTO registratsiya (id, user_number, user_name, user_surname, user_group, user_teacher, user_apply)
        VALUES ({},"{}", "{}", "{}", "{}", "{}");'''.format(id, phoneNumber, name, surname, group, teacher)).fetchall()