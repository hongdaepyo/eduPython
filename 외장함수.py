import os
os.getcwd()
os.system("ls -al")
os.system("cp test.txt test2.txt")

import shutil
shutil.copy("test.txt", "test2.txt")

import glob
glob.glob("*")

import tempfile
filename = tempfile.mkdtemp()

import time
time.time()
time.localtime(time.time())
time.asctime(time.localtime(time.time()))
time.ctime()
time.strftime('%c', time.localtime(time.time()))

for i in range(10):
    print(i)
    time.sleep(1)

import calendar
print(calendar.calendar(2019))
calendar.prcal(2016)
calendar.prmonth(2015, 6)
calendar.weekday(2015, 6, 30) #0~6 -> 0 = 월, 1 = 화 .... 6= 일
calendar.monthrange(2015,12)

import random
random.random()
random.randint(1, 10)
random.randint(1, 55)

def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))


def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

data = [1, 2, 3, 4, 5]
random.shuffle(data)
data

import webbrowser
webbrowser.open("http://gw.kaoni.com")
webbrowser.open_new("http://google.com")

#===================================================
import os
os.system("cd ../python")
dir = os.popen("dir")
print(dir.read())

import glob
glob.glob("doit/game/*.py")

import time
#2018/04/03 17:20:32
time.strftime("%Y/%m/%d %X ", time.localtime(time.time()))

import random
[random.randint(1, 45) for x in range(6)]

mstr = '''
|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|
'''
print(mstr)

import sys
testlist = []
while True:
    tmpstr = input() 
    if tmpstr == "":
        break
    else:
        testlist.append(tmpstr)
print("\n".join(testlist))