import re
import os

video = []  # тут хранится список архивов в папке %\video
for_remove = []  # список на удаление

#  Получаем список локальных дисков
def get_disks():
    disks = re.findall(r'[A-Z]+:.*$', os.popen('mountvol /').read(), re.MULTILINE)
    return disks

# Проверяем наличие папки VIDEO на обнаруженных дисках
def video_check():
    global video
    for letter in get_disks():
        if os.path.exists(path = letter + 'VIDEO'):
            print(f'Список объектов внутри каталога: {letter}VIDEO\\', os.listdir(path = letter + "VIDEO"), '\n')
            folders = os.listdir(path = letter + 'VIDEO')
            video.extend(folders[::])         
        else:
            #print(f'На диске {letter} такой папки не существует', '\n')
            continue

# Получаем список старых архивов
def oldArchive(month, year):
    ''' 
    1) на входе получаем список всех папок архивов
    2) вводим месяц, до которого требуется удалить все архивы
    3) формируем список на удаление
    4) выводим список для визуального подтверждения
    '''
    global video
    global for_remove
    # начинаем перебирать элементы в списке архивов
    for i in video:
        # from video folder dd-mm-yy hh format
        if int(i[3:5]) < month and int(i[6:8]) <= year:
        # заносим в список на удаление
            for_remove.append(i)
        else:
            continue
    print(*for_remove)

'''
Нужно разобраться с порядком вызова списка и вызова удаления
'''

# функция проверки ввода
def getInput():
    while True:
        getInput = input('Введите порядковый номер месяца: ')
        if getInput.isdigit():
            return getInput


# Запрашиваем ввод от пользователя
print('Введите порядковый номер месяца: ')
month = getInput()
print('Введите последние 2 цифры, обозначающие год: ')
year = getInput()

oldArchive(month, year)
