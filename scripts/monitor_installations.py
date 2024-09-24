from db_connector import game_monitoring_connector
from update_reddit_data_table import update_reddit_data_table

# Calculate the average installs per game in the last 7 days
def calculate_7days_average(cursor, game_id, days=7):
    avg_installs_query = """
        SELECT AVG(installs) 
        FROM installations 
        WHERE game_id = %s AND date >= CURDATE() - INTERVAL %s DAY
    """
    cursor.execute(avg_installs_query, (game_id, days))
    return cursor.fetchone()[0]


def monitor_installations(threshold_percentage=1.1):  # Example: 10% increase 
    db_connection = game_monitoring_connector()
    cursor = db_connection.cursor()

    # Fetch all game_ids
    cursor.execute("SELECT game_id FROM games")
    game_ids = cursor.fetchall()

    for (game_id,) in game_ids:
        # Get today's installations
        current_installs_query = """
            SELECT installs
            FROM installations
            WHERE game_id = %s AND date = CURDATE()
        """
        cursor.execute(current_installs_query, (game_id,))
        current_installs = cursor.fetchone()

        if current_installs:
            current_installs = current_installs[0]
            average_installs = calculate_7days_average(cursor, game_id)

            # Set dynamic threshold (number of installations)
            threshold = average_installs * threshold_percentage

            if current_installs > threshold:
                game_name_query = "SELECT game_name FROM games WHERE game_id = %s"
                cursor.execute(game_name_query, (game_id,))
                game_name = cursor.fetchone()
                print(f"{game_name} has passed it's threshold ({threshold}).")
                update_reddit_data_table(game_name) # Trigger collect reddit data about the game

    # Close the cursor and connection
    cursor.close()
    db_connection.close()

if __name__ == '__main__':
    monitor_installations()
