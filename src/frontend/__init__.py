# Format followed from: https://www.pygame.org/project-Python+Dungeon+Crawler-1266-.html
# More info from: https://docs.python.org/3/tutorial/modules.html
# and from: https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder

import os
files = os.listdir(os.path.join(os.path.abspath(""), 'frontend'))
for file in files:
    if file[-3:] == '.py' and file[:2] != '__':
        exec('from %s import *' % (file[:-3]))

__all__ = ['character', 'colors', 'item', 'window']
