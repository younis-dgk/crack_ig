#coding=utf-8
import os, sys, platform
 
os.system('rm -rf ig64.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf ig64.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ig64.so'):
        os.system('curl -L https://github.com/younis-dgk/crack_ig/blob/main/ig64.cpython-312.so?raw=true -o ig64.so') 
        import ig64
    else:
        import ig64
 
elif bit == '32bit':
    exit()
 
