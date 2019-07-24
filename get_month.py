import re
import os
from get_disks import get_disks
#from VIDEO_check import video

'''
Вычитаем из списка нужный месяц
'''

def get_month():
    video = ['01-01-19 00', '02-02-19 01', '03-03-19 02', '04-04-19 03', '02-01-19 03']
    video_str = ', '.join(video)
    print(video_str)
    # needed = []
    date =  input('Enter date: ')
    date = "'..." + date + "...'"
    for m in video_str:
        # result = re.findall(r'...01-19...', video_str)
        result = re.findall(date, video_str)
    for d in result:
        video = video.remove(d)
    return(result) 
    print(video)
get_month()
