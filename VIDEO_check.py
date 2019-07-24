import re
import os
from get_disks import get_disks

'''
Проверяем наличие папки VIDEO
'''
video = []
def VIDEO_check(video):
    for letter in get_disks():
        if os.path.exists(path = letter + 'VIDEO'):
            # print('Список объектов внутри: ', letter, os.listdir(path = letter + 'VIDEO'), '\n')
            folders = os.listdir(path = letter + 'VIDEO')
            video.extend(folders[::])         
        else:
            # print('На диске ', letter, 'такой папки не существует', '\n')
            continue
    return(video)