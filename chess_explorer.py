import api
import sys
import csv

if __name__ == '__main__':
    # print('\nWelcome to Chess Explorer!\n')
    # username = input('Enter a username to get started: ')
    
    # if not api.exists(username): 
    #     print('User not found')
    #     sys.exit()

    # while True:
    #     choice = input('\nmain menu\n--------\n(s)tats\ngame (h)istory\n(q)uit\n')
        
    #     if choice == 's': 
    #         api.get_stats_for(username)
    #     elif choice == 'q':
    #         sys.exit()
    #     elif choice == 'h':
    #         print('\nEnter month and year')
    #         month = input('Month (01-12): ')
    #         year = input('Year (YYYY): ')

    #         api.get_games_for(username, month, year)    
    #     else:
    #         print('Invalid selection')
        
    games = api.get_all_games("twopats")
    with open('games.csv', 'w') as games_csv:
        writer = csv.writer(games_csv)
        writer.writerow(['Date', 'Time', 'Time class', 'Played as', 'Outcome', 'Rating after', 'Opponent', 'Opp. rating'])
        for game in games:

            headers = getattr(game.game.get_pgn(), 'headers', {
                "EndDate": "",
                "EndTime": ""
            })
            
            writer.writerow([
                headers["EndDate"],
                headers["EndTime"],
                game.game.time_class, 
                game.played_as(), 
                game.result(), 
                game.ending_rating(), 
                game.opponent_name(),
                game.opponent_rating(),
            ])