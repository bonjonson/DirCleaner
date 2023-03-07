"""Небольшая утилита для удаления неактуальных директорий"""
import re
import os
import shutil
from datetime import datetime


archive_disks = []  # тут хранится словарь дисков с архивами
arch_list = {}  # словарь вида диск: папки
for_remove = []  # список на удаление
sysfold = ['INDEX', 'PROTECTED', 'INDEX_DATA', 'Settings.xml']  # список системных файлов и папок


def get_disks():
    '''Получаем список локальных дисков и удаляем из него элементы, 
    на которых не обнаружен каталог VIDEO'''
    arc_disks = re.findall(r'[A-Z]+:.*$', os.popen('mountvol /').read(), re.MULTILINE)
    vol_numbers = len(archive_disks)
    for letter in range(vol_numbers):
        if not os.path.exists(path = archive_disks[letter] + 'VIDEO'):
            archive_disks.pop(letter)
        else:
            continue
    return arc_disks


def archive_dir():
    '''Функция перебора все диски и составить список внутри директории VIDEO, 
    для этого создаем словарь из имен дисков'''
    arc_list = dict.fromkeys(archive_disks)  # создаем словарь с ключами по именам дисков
    for keys in arch_list:  # обходим словарь по ключам, обход поэлементный, а не поиндексный!
        arch_list[keys] = os.listdir(path = keys + 'VIDEO')
    return arc_list


def get_date():
    """получаем текующую месяц и год"""
    today = datetime.now()
    month = today.month
    year = today.year
    return month, year

current_month, current_year = get_date()


def get_last_archive(arc_list):
    ''' функция определения старого архива, старше 2 месяцев от текущей даты
    Выводим пользователю информацию о самых старых архивах на дисках и сразу 
    переопределяем словарь, оставляя только список на удаление'''
    most_last = []
    global for_remove
    for keys in arch_list:  # обходим ключи
        for dirs in arc_list.get(keys): # обходим значения
            if dirs not in sysfold:
                if current_year % 100 - int(dirs[6:8]) > 0:
                    # выполняем преобразование имени папки в формат yymm
                    most_last.append(str(dirs[6:8] + dirs[3:5]))
                    # тут же заносим эти папки в список на удаление
                    for_remove.append(dirs)
                elif current_year % 100 - int(dirs[6:8]) == 0 \
                    and current_month - int(dirs[3:5]) >= 3:
                    most_last.append(str(dirs[6:8] + dirs[3:5]))
                    for_remove.append(dirs)
            else:
                continue
        print(f'Самый старый архив на диске {keys}: {min(most_last)[2:4]}-{min(most_last)[:2]}')
        arch_list[keys] = for_remove # словарь вида диск: каталоги на удаление
        for_remove = [] # обнуляем список на удаление
    print(f'Список архивов на удаление на диске {arch_list}')


def old_arch_del():
    """функция рекурсивного удаления старых архивов"""
    for keys in arch_list:
        for dirs in arch_list.get(keys):
            arch_path = keys + 'VIDEO\\' + dirs
            print(arch_path)
            try:
                if os.path.isdir(arch_path):
                    shutil.rmtree(arch_path)
            except FileNotFoundError:
                continue


def sys_fold_del():
    """проверка наличия системных папок INDEX, PROTECTED, INDEX_DATA, файл Settings.xml"""
    for keys in arch_list:
        for folds in sysfold:
            sys_path = keys + 'VIDEO\\' + folds
            print(sys_path)
            try:
                if os.path.isfile(sys_path):
                    os.unlink(sys_path)
                elif os.path.isdir(sys_path):
                    shutil.rmtree(sys_path)
            except FileNotFoundError:
                continue

archive_disks = get_disks()
arch_list = archive_dir()
get_last_archive()
old_arch_del()
sys_fold_del()
