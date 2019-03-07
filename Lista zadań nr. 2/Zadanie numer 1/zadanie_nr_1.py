import datetime


class Note(object):
    staticID = 0

    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
        date = datetime.datetime.now()
        Note.staticID += 1
        self.ID = Note.staticID

    def match(self):
        True if isinstance(self.text, char) or isinstance(self.tag, char) else False

class Notebook(Note):

    def __init__(self):
        self.notes = []

    def new_note(self):
        self.notes.append(Note.)
