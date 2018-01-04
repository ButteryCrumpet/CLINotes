""" Note db connection class """

import sqlite3
import os 

class NotesDB(object):

    def __init__(self, db_path='default'):
        if db_path == 'default':
            db_path = self.get_default_path()
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.initTables()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def insert_note(self, note):
        sql = ('INSERT INTO notes(content, modified, group_id)'
               'VALUES (?, ?, ?)')
        group_pid = self.get_group_pid(note.group)
        data = (note.content, note.modified, group_pid)
        self.cursor.execute(sql, data)
        self.conn.commit()

    def get_all_notes(self):
        sql = ('SELECT * FROM notes')
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_note(self, note_id):
        sql = ('SELECT notes.content, groups.name, notes.modified, notes.pid '
               'FROM notes '
               'INNER JOIN groups ON notes.group_id = groups.pid '
               'WHERE notes.pid=(?)')
        self.cursor.execute(sql, (note_id,));
        return self.cursor.fetchone()

    def update_note(self, note):
        return

    def delete_note(self, note_id):
        sql = ('DELETE FROM notes WHERE pid = (?)')
        self.cursor.execute(sql, (note_id, ))
        return

    def insert_group(self, group_name):
        sql = ('INSERT INTO groups(name)'
               'VALUES (?)')
        self.cursor.execute(sql, (group_name,))
        self.conn.commit()

    def get_group_pid(self, group_name):
        sql = ('SELECT pid FROM groups WHERE name = (?)')
        self.cursor.execute(sql, (group_name,))
        item = self.cursor.fetchone();
        return item[0]

    def get_groups(self):
        sql = ('SELECT name FROM groups')
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def initTables(self):
        sql = ('CREATE TABLE IF NOT EXISTS notes('
               'pid INTEGER PRIMARY KEY,'
               'content TEXT NOT NULL,'
               'modified INTEGER NOT NULL,'
               'group_id INTEGER NOT NULL'
               ')')
        self.cursor.execute(sql)

        sql = ('CREATE TABLE IF NOT EXISTS groups('
               'pid INTEGER PRIMARY KEY,'
               'name TEXT NOT NULL UNIQUE'
               ')') 
        self.cursor.execute(sql)

    def get_default_path(self):
        currdir = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(currdir, 'notes.db')

def main():
    currdir = os.path.dirname(os.path.realpath(__file__))
    print(os.path.join(currdir, 'notes.db'))

if __name__ == '__main__':
    main()