import re
import os
import get_disks
import VIDEO_check

'''
Определяем блоки по месяцам
'''
def get_month():
    m = input('Введите номер месяца в двузначном формате: ')
    # m = re.findall('...' + m + '......',VIDEO_check.VIDEO_check())
    for mm in VIDEO_check.VIDEO_check():
        month = re.match(r'...' + m + '......', mm)
        print('Обнаружены следующие объекты: ', month, end = '\n')
    return(month)