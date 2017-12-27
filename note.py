""" Note class module. """

import time

class Note(object):
    """ Note class """

    def __init__(self, content, group='General', modified=time.time(), nid=-1):
        self.content = content
        self.group = group
        self.modified = modified
        self.nid = nid
  
    def update_modified(self, time):
        self.edited = time.time()

    def __repr__(self):
        return str(self.nid) + ' | ' + self.content + ' | ' + str(self.group)
