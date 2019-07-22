import re
import os
import get_disks
'''
Проверяем наличие папки VIDEO
'''
def VIDEO_check():
    for letter in get_disks.get_disks():
        if os.path.exists(path = letter + 'VIDEO'):
            print('Список объектов внутри: ', letter, os.listdir(path = letter + 'VIDEO'), '\n')
            video = os.listdir(path = letter + 'VIDEO')
        else:
            print('На диске ', letter, 'такой папки не существует', '\n')
    return(video)