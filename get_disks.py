import re, os
'''
Получаем список дисков в системе
'''
def get_disks():
    disks = re.findall(r'[A-Z]+:.*$', os.popen('mountvol /').read(), re.MULTILINE)
    return(disks)
