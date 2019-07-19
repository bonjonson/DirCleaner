import os
import re

'''
Получаем список дисков в системе
'''
def get_disks():
    disks = re.findall(r'[A-Z]+:.*$', os.popen('mountvol /').read(), re.MULTILINE)
    return(disks)
# Вызываем список дисков
get_disks()

'''
Проверяем наличие папки VIDEO
'''
def VIDEO_check():
    for letter in get_disks():
        if os.path.exists(path = letter + 'VIDEO'):
            print('Список объектов внутри: ', letter, os.listdir(path = letter + 'VIDEO'), '\n')
            video = os.listdir(path = letter + 'VIDEO')
        else:
            print('На других дисках такой папки не существует', '\n')
    return(video)

VIDEO_check()
