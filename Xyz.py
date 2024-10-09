import os,re,sys,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    import ig64
elif bit == '32bit':
    print(f"\033[1;91m Sorry Baby 32 Bit Not Supported .... ");exit() 
 
 
