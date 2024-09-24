from google_play_scraper import app
from datetime import date

# Get the current installs from Google Play Store
def get_current_installs(app_id):
    try:
        result = app(app_id)
        installs = result['realInstalls']
    except Exception as e:
        print(f"Error fetching installs for {app_id}: {e}")
        installs = None
    return installs

def update_installations_table(cursor):
    current_date = date.today().strftime("%Y-%m-%d")

    # Fetch all game_ids and app_ids of all games
    query = "SELECT game_id, app_id FROM games"
    cursor.execute(query)
    games = cursor.fetchall()

    # Insert a new installation record for each game
    for (game_id, app_id) in games:
        installations = get_current_installs(app_id)  # Get actual installation count

        # Check if the record already exists
        check_query = "SELECT COUNT(*) FROM installations WHERE game_id = %s AND date = %s"
        cursor.execute(check_query, (game_id, current_date))
        exists = cursor.fetchone()[0]

        if exists == 0:  # If no existing record
            # Insert into installations table
            insert_query = "INSERT INTO installations (game_id, date, installs) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (game_id, current_date, installations))
        else:
            print(f"Record for game_id {game_id} on date {current_date} already exists.")

    print("Installations table updated successfully.")