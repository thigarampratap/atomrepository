import os
import sys

print('current work directory is : ', os.getcwd())
print('python version is ', sys.version)
rpl = os.getcwd().replace('\\','/')
print(rpl)
spl = rpl.split('/')
for folder, subfolder, filenames in os.walk('c:/Users/'):
    sze = 0
    found = True
    for file in filenames:
        try:
            sze += round(((os.stat(file).st_size)/(1024*1024)),4)
            if sze >= 5 and found:
                print('Folder:', folder)
                print('subfolder:', subfolder)
                print('-' * 80)
                print('file name : {} & its size: {} MB'.format(file, sze))
                print('-' * 80)
                print('=' * 80)
                found = False
        except:
            pass
