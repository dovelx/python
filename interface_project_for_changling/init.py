import os
import time

from htmlreporter import HtmlReport
# for i in range(30):
#     os.system("python mainxx.py")
#init  s3 s4 s11 s12 s13 s16 s17
os.system("python s3.py 0")

os.system("python s3.py 1")
time.sleep(1)
os.system("python s4.py 0 ")
os.system("python s4.py 1")
time.sleep(1)
os.system("python s12.py 0")
os.system("python s12.py 1")
time.sleep(1)
os.system("python s13.py 0")
os.system("python s13.py 1")
time.sleep(1)
os.system("python s16.py")
time.sleep(1)
os.system("python s17.py")
time.sleep(1)
os.system("python s11.py")
