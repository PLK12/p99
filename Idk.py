import os
import shutil
import time
path = input("Enter name here")
days = os.time.time(path)
if os.path.exists(path+"/"+ext):
    os.walk(path)
    os.path.join()
ctime = os.stat(path).st_ctime
    