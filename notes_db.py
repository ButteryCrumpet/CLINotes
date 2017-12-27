""" Note db connection class """

import sqlite3

class NotesDB(object):

    def __init__(self, db_path='notes.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.initTables()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def insert_note(self, note):
        sql = ('INSERT INTO notes(CONTENT, MODIFIED, GROUP_ID)'
               'VALUES (?, ?, ?)')
        data = (note.content, note.modified, note.group)
        self.cursor.execute(sql, data)
        self.conn.commit()

    def get_note(self, note_id):
        sql = ('SELECT * FROM notes WHERE ID=(?)')
        self.cursor.execute(sql, (note_id,));
        return self.cursor.fetchall()

    def update_note(self, note):
        return

    def delete_note(self, note):
        return

    def initTables(self):
        sql = ('CREATE TABLE IF NOT EXISTS notes('
               'ID INTEGER PRIMARY KEY,'
               'CONTENT TEXT NOT NULL,'
               'MODIFIED INTEGER NOT NULL,'
               'GROUP_ID INTEGER NOT NULL'
               ')')
        self.cursor.execute(sql)

        sql = ('CREATE TABLE IF NOT EXISTS groups('
               'ID INT PRIMARY KEY NOT NULL,'
               'NAME TEXT NOT NULL'
               ')') 
        self.cursor.execute(sql)
