import re
import os
from get_disks import get_disks
from VIDEO_check import VIDEO_check
# from get_month import get_month
video = []

get_disks()
VIDEO_check(video)
print(video)