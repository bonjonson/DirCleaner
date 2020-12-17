import re
import os


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
            # video = os.listdir(path = letter + 'VIDEO')
            # arch_list[keys] = video  # сохраняем значение в виде списка в ключ
            arch_list[keys] = os.listdir(path = letter + 'VIDEO')


'''
1) добавить функцию по аналогии с oldArchive с ручным выбором диска
2) добавить вызовы функций из бесконечного цикла пользовательским вводом, типа show archive и тд'''


# Получаем список старых архивов
def oldArchive(month, year):
    global for_remove
    video = []
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
