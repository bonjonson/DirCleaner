import re
import os
from datetime import datetime


archive_disks = []  # тут хранится словарь дисков с архивами
arch_list = {}  # словарь вида диск: папки
for_remove = []  # список на удаление

#  Получаем список локальных дисков и удаляем из него элементы, на которых не обнаружен каталог VIDEO
def get_disks():
    global archive_disks
    archive_disks = re.findall(r'[A-Z]+:.*$', os.popen('mountvol /').read(), re.MULTILINE)
    for letter in range(len(archive_disks)):
        if not os.path.exists(path = archive_disks[letter] + 'VIDEO'):
            archive_disks.pop(letter)
        else:
            continue

# тут мы должны перебрать все диски и составить список внутри директории VIDEO, для этого создаем словарь из имен дисков
def archiveDir():
    global arch_list
    arch_list = dict.fromkeys(archive_disks)  # создаем словарь с ключами по именам дисков
    for keys in arch_list:  # обходим словарь по ключам, обход поэлементный, а не поиндексный!
        arch_list[keys] = os.listdir(path = keys + 'VIDEO')

# получаем текующую месяц и год
def get_date():
    today = datetime.now()
    month = today.month
    year = today.year
    return month, year

current_month, current_year = get_date() 

''' функция определения старого архива, старше 2 месяцев от текущей даты
Выводим пользователю информацию о самых старых архивах на дисках и сразу переопределяем словарь, оставляя только список на удаление'''
def getLastArchive():
    most_last = []
    global for_remove
    for keys in arch_list:  # обходим ключи
        for dirs in arch_list.get(keys): # обходим значения
            if current_year % 100 - int(dirs[6:8]) > 0:
                # выполняем преобразование имени папки в формат yymm
                most_last.append(str(dirs[6:8] + dirs[3:5]))
                # тут же заносим эти папки в список на удаление
                for_remove.append(dirs)
            elif current_year % 100 - int(dirs[6:8]) == 0 and current_month - int(dirs[3:5]) >= 2:
                most_last.append(str(dirs[6:8] + dirs[3:5]))
                for_remove.append(dirs)
        print(f'Самый старый архив на диске {keys}: {min(most_last)[2:4]}-{min(most_last)[:2]}')
        arch_list[keys] = for_remove  # словарь вида диск: каталоги на удаление
        for_remove = []  # обнуляем список на удаление 
    print(f'Список архивов на удаление на диске {arch_list}')


# функция рекурсивного удаления старых архивов
def oldArchDel():
    for keys in arch_list:
        for dirs in arch_list.get(keys):
            path = keys + 'test\\' + dirs
            print(path)
            try:
                if os.path.exists(path = path) and os.path.isdir(path):
                    shutil.rmtree(path)
            except:
                continue

# проверка наличия системных папок INDEX, PROTECTED, INDEX_DATA, файл Settings.xml
def sysFoldDel():
    sysfold = ['INDEX', 'PROTECTED', 'INDEX_DATA', 'Settings.xml']
    for keys in arch_list:
        for folds in sysfold:
            path = keys + 'VIDEO\\' + folds
            try:
                if os.path.isfile(path):
                    os.unlink(path)
                elif os.path.isdir(path):
                    shutil.rmtree(path)
            except:
                continue
get_disks()
archiveDir()
getLastArchive()
oldArchDel()
sysFoldDel()