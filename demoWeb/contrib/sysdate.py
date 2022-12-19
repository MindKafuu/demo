'''
17/1/2018   Jirapong Initial verion
'''

from datetime import datetime,time,date,timedelta
from django.utils import timezone

__monthList = ['มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'สิงหาคม', 'กันยายน',
               'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']


def __dateFromThaiBuddhist(dt):
    try:
        dt = '{}{}'.format(dt[:-4], int(dt[-4:]) - 543)
        dt = datetime.strptime(dt, "%d/%m/%Y")
        return dt.replace(tzinfo=timezone.utc)
    except:
        return


def striptime(dt=datetime.now()):
    if dt is None:
        return dt
    if type(dt) == datetime.date:
        dt = datetime.combine(dt,time.min)
    elif type(dt) == datetime:
        dt = datetime.combine(dt.date(),time.min)
    if type(dt) == date:
        dt = datetime.combine(dt,time.min)
    return dt


def stringtodatetime(dt='',fmt='%Y-%m-%d %H:%M:%S.%f'):
    dt = dt.strip()
    try:
        if dt == '' :
            return
        else :
            return datetime.strptime(dt,fmt)
    except:
        return


def daysafter(src=None, dst=None):
    if not src: src = datetime.now()
    if not dst: dst = datetime.now()
    if type(src) == datetime:
        src = src.date()
    if type(dst) == datetime:
        dst = dst.date()
    return (src-dst).days


def dateFromLocal(dt):
    return __dateFromThaiBuddhist(dt)
