from db_connector import game_monitoring_connector

# Calculate the average installs per game in the last 7 days
def calculate_moving_average(cursor, game_id, days=7):
    avg_installs_query = """
        SELECT AVG(installs) 
        FROM installations 
        WHERE game_id = %s AND date >= CURDATE() - INTERVAL %s DAY
    """
    cursor.execute(avg_installs_query, (game_id, days))
    return cursor.fetchone()[0]


def monitor_installations(threshold_percentage=1.2):  # Example: 20% increase
    db_connection = game_monitoring_connector()
    cursor = db_connection.cursor()

    # Fetch all game_ids
    cursor.execute("SELECT game_id FROM games")
    game_ids = cursor.fetchall()
    print(game_ids)

monitor_installations()
#     for (game_id,) in game_ids:
#         # Get today's installations
#         current_installs_query = "SELECT installs FROM installations WHERE game_id = %s AND date = CURDATE()"
#         cursor.execute(current_installs_query, (game_id,))
#         current_installs = cursor.fetchone()

#         if current_installs:
#             current_installs = current_installs[0]
#             # Calculate moving average
#             moving_average = calculate_moving_average(cursor, game_id)

#             if moving_average is not None:
#                 # Set dynamic threshold
#                 threshold = moving_average * threshold_percentage

#                 if current_installs > threshold:
#                     send_alert(game_id, current_installs)  # Trigger your alerting system

#     # Close the cursor and connection
#     cursor.close()
#     db_connection.close()

# # Schedule this function to run daily
# monitor_installations()
