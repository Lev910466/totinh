from pydoc import stripid
from tqdm import tqdm 
import sys
from colorama import Fore, Back , Style
from colorama import init, AnsiToWin32
import time
from alive_progress import alive_bar
import threading
import os
# started + yellow
print("WELCOME")
init(wrap=False )
stream3 = AnsiToWin32(sys.stderr).stream 
print(Fore.YELLOW, file=stream3)
time.sleep (0.1)
# loading bar 1
loop = tqdm(total = 5000, position = 0 , leave = False )
for k in range (5000):
    loop.set_description ("loading...".format(k))
    loop.update (1)
loop.close()
time.sleep (0.1)
print("YOUR NAME : ")
a= input()
print("YOUR CRUSH NAME : ")
b = input()
print("IT'S CORRECT")
time.sleep(0.5)

# error code 1 + red COLORAMA + end
init(wrap=False )
stream = AnsiToWin32(sys.stderr).stream 
print(Fore.RED, file=stream)
with open('errorcode1') as rf:
    line = rf.readline()
    index = 1
    while line:
        print(line )
        time.sleep(0.005)
        index += 1
        line = rf.readline()
print(Style.RESET_ALL)

# bar2 + colorama green
init(wrap=False )
stream1 = AnsiToWin32(sys.stderr).stream 
print(Fore.GREEN, file=stream1)
bar_l = 100
with alive_bar(bar_l) as bar:
    for i in range(bar_l):
        time.sleep(0.03)
        bar()

done = 'false'
#the animation loading
def animate():
    for i in range (5):
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')
animate()
print(Style.RESET_ALL)

# acii my img
time.sleep (1)
f = open('myimg.txt')
line_1 = f.read()
for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    time.sleep(0.001)
print("k",'\n')
time.sleep(1)
# the animation 2 + cyan colorama
init(wrap=False )
stream2 = AnsiToWin32(sys.stderr).stream 
print(Fore.CYAN, file=stream2)
def load_animation():
    load_str = "starting your console application..."
    ls_len = len(load_str)  
    animation = "|/-\\"
    anicount = 0
    counttime = 0        
    i = 0                       
    while (counttime != 100):        
        time.sleep(0.075)       
        load_str_list = list(load_str)             
        x = ord(load_str_list[i])               
        y = 0                                  
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)                
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]       
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()       
        load_str = res         
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1   
    if os.name =="nt":
        os.system("cls")   
    else:
        os.system("clear") 
if __name__ == '__main__': 
    load_animation()  
    s ="HA-pipiu"
    sys.stdout.write("Hello "+str(s)+"\n")
    time.sleep(1)

# acii ILY + magenta clolorama
init(wrap=False )
stream4 = AnsiToWin32(sys.stderr).stream 
print(Fore.MAGENTA, file=stream4)
f2 = open('iloveyou.txt')
line_2 = f2.read()
for x in line_2:
    print(x, end='')
    sys.stdout.flush()
    time.sleep(0.001)
print("k",'\n')
time.sleep (1)

# errorcode 2 + green colorama 
init(wrap=False )
stream = AnsiToWin32(sys.stderr).stream 
print(Fore.GREEN , file=stream)
with open('errorcode2') as rf:
    line = rf.readline()
    index = 1
    while line:
        print(line )
        time.sleep(0.005)
        index += 1
        line = rf.readline()
print(Style.RESET_ALL)

# bar3 + colorama green + loadingg animation 
init(wrap=False )
stream5 = AnsiToWin32(sys.stderr).stream 
print(Fore.GREEN, file=stream5)
bar_l = 100
with alive_bar(bar_l) as bar:
    for i in range(bar_l):
        time.sleep(0.03)
        bar()
def animate():
    for i in range (5):
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')
animate()
print(Style.RESET_ALL)

# acii tt + RED COLORAMA 
init(wrap=False )
stream6 = AnsiToWin32(sys.stderr).stream 
print(Fore.RED, file=stream6)
f3 = open('tt.txt')
line_3 = f3.read()
for x in line_3:
    print(x, end='')
    sys.stdout.flush()
    time.sleep(0.001)
print("k",'\n')