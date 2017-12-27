""" Note class module. """

import time

class Note(object):
    """ Note class """

    def __init__(self, content, group=1, modified=time.time(), nid=-1):
        self.content = content
        self.group = group
        self.modified = modified
        self.nid = nid

    def get_content(self):
        return self.content

    def update_content(self, content):
        self.content = content

    def get_group(self):
        return self.group

    def update_group(self, group):
        self.group = group
  
    def update_edited(self, time):
        self.edited = time
