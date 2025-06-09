#IMPORTS

import os
from random import randint
from colorama import Fore,init,Back
import colorama
import sys
from pytimedinput import timedInput
import time
import msvcrt

#DISPLAY FUNCTIONS

def screen():
    for cell in CELLS:  
        if cell in bar_right:
            print(Fore.MAGENTA + "I",end="")
        elif cell in bar_left:
            print(Fore.MAGENTA  + "I",end="")
        elif cell==tuple(ball):
            print(Fore.GREEN + "o",end="")
        elif cell[1] in (0,screen_y-1) or cell[0] in (0,screen_x-1):
            print(Fore.RED + "#",end="")
        else:
            print(" ",end="")
        if cell[0]==screen_x-1:
            print("")       
def start_screen_play():    
    os.system("cls")
    print(Fore.YELLOW + '''
     _____
    |  _  \\
    | |_|  |____  _ __   ____ 
    |  __  / _  \\| '_ \\ / _  \\
    | |   | |_|  | | | | |_|  |
    |_|    \\____/|_| |_|\\__  /
                       ___| |
                      \\ ____/
    
    
    PONG GAME BY BLUE BOI
            
''')
    print("            ",Fore.YELLOW + Back.WHITE + "PLAY")
    print("            ",Fore.YELLOW + "EXIT")
def start_screen_exit():    
    os.system("cls")
    print(Fore.YELLOW + '''
     _____
    |  _  \\
    | |_|  |____  _ __   ____ 
    |  __  / _  \\| '_ \\ / _  \\
    | |   | |_|  | | | | |_|  |
    |_|    \\____/|_| |_|\\__  /
                       ___| |
                      \\ ____/
    
    
    PONG GAME BY BLUE BOI
            
''')
    print("            ",Fore.YELLOW + "PLAY")
    print("            ",Fore.YELLOW + Back.WHITE + "EXIT")

#GAME FUNCTIONS

def paddle_move(dir):
    global bar_right
    if dir=="w":
        if bar_right[0][1]!=1:
            bar_right.pop(2)
            first_item=list(bar_right[0])
            first_item[1]-=1
            first_item=tuple(first_item)
            bar_right.append(first_item)
            bar_right.sort()
    elif dir=="s":
        if bar_right[2][1]!=14:
            bar_right.pop(0)
            first_item=list(bar_right[1])
            first_item[1]+=1
            first_item=tuple(first_item)
            bar_right.append(first_item)
            bar_right.sort()
def direction_change():
    global ball,direction
    if ball[1]==1:
        direction[1]="DOWN"
    if ball[1]==14:
        direction[1]="UP"
    if ball[0]==3:
        direction[0]="RIGHT"
    if ball[0]==36:
        if ball[1]==bar_right[0][1] or ball[1]==bar_right[1][1] or ball[1]==bar_right[2][1]:
            direction[0]="LEFT"
def move_ball():
    global ball
    if direction==["RIGHT","UP"]:
        ball[0]+=1#
        ball[1]-=1#
    if direction==["RIGHT","DOWN"]:
        ball[0]+=1#
        ball[1]+=1#
    if direction==["LEFT","UP"]:
        ball[0]-=1
        ball[1]-=1
    if direction==["LEFT","DOWN"]:
        ball[0]-=1
        ball[1]+=1
def lose_game():
    global Resume
    os.system("cls")
    print('''
            
                              You Lose !
            
         
         00   00               00                             000
          00 00                00                             000 
           000  0000  00  00   00      0000  /0000   0000     000
           00  00  00 00  00   00     00  00   \\\\   0 --00    000
           00   0000   0000    000000  0000  0000/  \\0000     ***
               
            ''')
    time.sleep(4)
    start_screen_play()
    Resume=False
    time.sleep(0.3)

#MAIN GAME FUNCTION

def GAME():
    global Resume,move_user
    while Resume:
        sys.stdout.write('\x1b[17A')
        screen()
        direction_change()
        move_user,_ = timedInput("",timeout = 0.06)
        if move_user=="q":
            start_screen_play()
            Resume=False
            time.sleep(0.3)
        paddle_move(move_user)
        move_ball()
        if ball[0]==38:
            lose_game()

#GLOBAL VARIABLES

screen_x=40
screen_y=16

bar_left=[(2,y_len) for y_len in range(1,15)]
bar_right=[(screen_x-3,y_len) for y_len in range(screen_y//2-1,screen_y//2+2)]
ball=[17,7]

CELLS=[(x,y) for y  in range(screen_y) for x in range(screen_x)]

Resume=False
FullGameExit=True
selected_option="PLAY"
random_num_1=randint(0,1)
random_num_2=randint(0,1)
direction=["RIGHT","UP"]
if random_num_1==0:
    direction[0]="RIGHT"
else:
    direction[0]="LEFT"
if random_num_2==0:
    direction[1]="UP"
else:
    direction[1]="DOWN"

#INITIALISATION

colorama.init()
init(autoreset=True)

os.system("cls")
start_screen_play()

#MAIN GAME LOOP

while FullGameExit:    
    bar_right=[(screen_x-3,y_len) for y_len in range(screen_y//2-1,screen_y//2+2)]
    ball=[17,7]
    choose = msvcrt.getch().decode("utf-8")
    if choose=="s" and selected_option=="PLAY":
        selected_option="EXIT"
        start_screen_exit()
    elif choose=="w" and selected_option=="EXIT":
        selected_option="PLAY"
        start_screen_play()
    else:
        if choose==" " and selected_option=="PLAY":
            os.system("cls")
            Resume=True
        elif choose==" " and selected_option=="EXIT":
            os.system("cls")
            FullGameExit=False
    if Resume==True:
        GAME()
