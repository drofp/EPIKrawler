# Author Vinh Truong

class Item(object):

    def __init__(self, name: str, picture: 'picture'):
        self.name = name
        self.picture = picture
    
    def set_name(self, new_name):
        self.name = new_name
    
    def set_picture(self, new_picture):
        self.picture = new_picture