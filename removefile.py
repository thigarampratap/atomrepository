import os

if os.path.exists('delfile.py'):
	print(os.remove('delfile.py'))
	print('delfile is deleted *** ')
else:
    print('delfile is not found !!!')
