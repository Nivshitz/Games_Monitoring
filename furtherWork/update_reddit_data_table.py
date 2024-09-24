from datetime import date, datetime, timedelta

def get_reddit_game_data(game_name=None):
    search_end_date = date.today() # Current date
    search_start_date = search_end_date - timedelta(days=7) # 7 days before today
    print("conncecting to Reddit API and getting the last week's data about {game_name}.")

def update_reddit_data_table():
    get_reddit_game_data()
    # insert the data into the table the table

if __name__ == '__main__':
    update_reddit_data_table()