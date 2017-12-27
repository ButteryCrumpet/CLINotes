
from note import Note
from notes_db import NotesDB

class NotesRun(object):

    def __init__(self):
        self.db = NotesDB()

    def create_note(self, content, group='General'):
        note = Note(content, group)
        self.db.insert_note(note)

    def get_note(self, note_id):
        query = self.db.get_note(note_id)
        note = Note(query[0], query[1], query[2], query[3])
        print note

    def create_group(self, group_name):
        self.db.insert_group(group_name)

    def show_groups(self):
        groups = self.db.get_groups();
        for group in groups:
            print group[0]