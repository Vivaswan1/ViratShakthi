#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 02:31:38 2021

@author: Vivaswan1 ( v-goddevil )
"""
import random
pre_assume = random.randint(0,9)

attempt = 0
limit = 3

start_game = input('enter yes or no:').lower()

while start_game != 'yes' and start_game != 'no':
    print('invalid option... enter yes / no')
    start_game = input('enter yes or no:').lower()
else: 

    if start_game == 'no':
        print(f'thank you....')
    
    elif start_game == 'yes':
    
        while attempt < limit:
            
            try:
                    
                guess = int(input('Guess the number from 0-9 : '))
                
                if guess < 0 or guess > 9:
                    raise ValueError(f" Please enter the number from 0 to 9..... ")
                        
                attempt +=1
                        
                if guess == pre_assume:
                    print(f'congrats you guessed number....  ')
                    break
            except ValueError as error:
                print(f'invald nuymber.. try again... {error}')
        else:
             print(f'sorry you are failed... better luck next time...')
