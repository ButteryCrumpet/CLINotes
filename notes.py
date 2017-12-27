
from note import Note
from notes_db import NotesDB

class NotesRun(object):

    def __init__(self):
        self.db = NotesDB()

    def create_note(self, content, group=1):
        note = Note(content, group)
        self.db.insert_note(note)

    def get_note(self, note_id):
        print self.db.get_note(note_id)
