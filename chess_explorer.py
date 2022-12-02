#!/usr/bin/python3

import api
import sys

if __name__ == '__main__':
    print('\nWelcome to Chess Explorer!\n')
    username = input('Enter a username to get started:\n')
    
    if not api.exists(username): 
        print('User not found')
        sys.exit()

    choice = input('(1) stats\n(2) game history\n')
    
    if choice == '1': 
        api.get_stats_for(username)
        sys.exit()
    elif choice != '2':
        print('Invalid selection')
        sys.exit()
    
    print('Enter month and year')
    month = input('Month (1-12): ')
    year = input('Year (YYYY): ')

    api.get_games_for(username, month, year)