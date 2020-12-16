import re
import os

disks_dict = {}  # test dict
archive_disks = {}  # тут хранится словарь дисков с архивами
video = []  # тут хранится список всех архивов в папке %\video
for_remove = []  # список на удаление

#  Получаем список локальных дисков
def get_disks():
    global disks_dict
    disks = re.findall(r'[A-Z]+:.*$', os.popen('mountvol /').read(), re.MULTILINE)
    disks_dict = dict.fromkeys(disks)  # ключи создаются в неподходящем формате "c:\\"
    print(disks_dict)
    return disks

# Возвращает список дисков, на которых обнаружены папки
def diskList():
    global archive_disks
    local_disks_dict = {}
    for letter in get_disks():
        if os.path.exists(path = letter + 'VIDEO'):
            # создаем пары key: None, где ключ это имя диска
            local_disks_dict = dict.fromkeys(letter)
            # обновляем глобальный словарь с именами дисков в которых есть архивы
            archive_disks.update(local_disks_dict)
        else:
            continue

''' разобраться в каком виде вызывать video_check()'''

# Проверяем наличие папки VIDEO на обнаруженных дисках
def video_check():
    global video
    for letter in get_disks():
        if os.path.exists(path = letter + 'VIDEO'):
            print(f'Список объектов внутри каталога: {letter}VIDEO\\', os.listdir(path = letter + "VIDEO"), '\n')
            folders = os.listdir(path = letter + 'VIDEO')
            video.extend(folders[::])         
        else:
            continue

'''
1) добавить функцию по аналогии с oldArchive с ручным выбором диска
2) добавить вызовы функций из бесконечного цикла пользовательским вводом, типа show archive и тд'''


# Получаем список старых архивов
def oldArchive(month, year):
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
1) добавить выбор диска, на котором проводим поиск и готовим список на удаление
2) 
'''

# функция проверки ввода
def getInput():
    while True:
        getInput = input('Введите порядковый номер месяца: ')
        if getInput.isdigit() and len(getInput) <= 2:
            return getInput


# Запрашиваем ввод от пользователя
print('Введите порядковый номер месяца: ')
month = getInput()
print('Введите последние 2 цифры, обозначающие год: ')
year = getInput()

oldArchive(month, year)
