import os
import sys
import time,datetime
if __name__ == '__main__':
    if(len(sys.argv) == 3 and len(sys.argv[2]) == 8):
        type = sys.argv[1]
        ct = sys.argv[2]
        year = int(ct[0:4])
        month = int(ct[4:6])
        day = int(ct[6:8])
        current_time = datetime.date(year, month, day)
    else:
        type = sys.argv[1]
        current_time = datetime.date.today()
print type
print current_time

