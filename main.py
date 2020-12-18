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
        for letter in archive_disks:  # обходим внутри диска содержимое директорий в папке VIDEO
            arch_list[keys] = os.listdir(path = letter + 'VIDEO')

# получаем текующую месяц и год
def get_date():
    today = datetime.now()
    month = today.month
    year = today.year
    return month, year

current_month, current_year = get_date() 

''' функция определения старого архива, старше 2 месяцев от текущей даты
Выводим пользователю информацию о самых старых архивах на дисках'''
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
        print(f'Список архивов на удаление на диске {keys}: {for_remove}')

'''здесь будет добавлена фунция получения самого старого архива на каждом из дисков
'''


'''
1) добавить функцию по аналогии с oldArchive с ручным выбором диска
2) добавить вызовы функций из бесконечного цикла пользовательским вводом, типа show archive и тд'''


# # Получаем список старых архивов
# def oldArchive(month, year):
#     global for_remove
#     video = []
#     # начинаем перебирать элементы в списке архивов
#     for i in video:
#         # from video folder dd-mm-yy hh format
#         if int(i[3:5]) < month and int(i[6:8]) <= year:
#         # заносим в список на удаление
#             for_remove.append(i)
#         else:
#             continue
#     print(*for_remove)

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

# oldArchive(month, year)
