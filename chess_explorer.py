#!/usr/bin/python3

import api
import sys

if __name__ == '__main__':
    print('\nWelcome to Chess Explorer!\n')
    username = input('Enter a username to get started: ')
    
    if not api.exists(username): 
        print('User not found')
        sys.exit()

    while True:
        choice = input('\nmain menu\n--------\n(s)tats\ngame (h)istory\n(q)uit\n')
        
        if choice == 's': 
            api.get_stats_for(username)
        elif choice == 'q':
            sys.exit()
        elif choice == 'h':
            print('\nEnter month and year')
            month = input('Month (01-12): ')
            year = input('Year (YYYY): ')

            api.get_games_for(username, month, year)    
        else:
            print('Invalid selection')
        