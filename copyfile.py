import shutil
import os

# C:/Users/prata/Desktop/py38/pypgm
# cp = os.path.splitext('C:/Users/prata/Desktop/py38/')
print('before: ', os.listdir('C:/Users/prata/Desktop/py38/pypgm'))
shutil.move('C:/Users/prata/Desktop/py38/pdpgm.py', 'C:/Users/prata/Desktop/py38/pypgm')
print('after: ', os.listdir('C:/Users/prata/Desktop/py38/pypgm'))
