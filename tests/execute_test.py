import subprocess
import time

command1 = subprocess.Popen(['D:\\test.exe', '100', '100', '1300', '0.52', '300', '1', '1', '1', '0.34', '0.27', '3', '10', '100000', '300000', '0'])
#D:\test.exe 100 100 1300 0.52 300 1 1 1 0.34 0.27 3 10 100000 300000 0
print('komnunikaty wyjscia')

i = 0

while True:
    time.sleep(1)
    print(str(i)+')\n '+str(command1.stdout))
    print('state: ', command1)
    i+=1