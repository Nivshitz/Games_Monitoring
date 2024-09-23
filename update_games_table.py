import pandas as pd
from db_connector import game_monitoring_connector

db_connection = game_monitoring_connector()

data = {
    'game_name': ['Pirate Kings', 'Raid Heroes: Total War', 'Piggy GO', 'Board Kings', 'Animals & Coins Adventure Game'],
    'developer_name': ['Jelly Button Games', 'Persona Games', 'Forever9 Games', 'Jelly Button Games', 'Innplay Labs'],
    'app_id': ['com.jellybtn.cashkingmobile', 'com.raid.heroes.total.war', 'com.aladinfun.piggytravel.android', 'com.jellybtn.boardkings', 'com.innplaylabs.animalkingdomraid']
}

df_games = pd.DataFrame(data)
print(df_games)

# Create a cursor object
cursor = db_connection.cursor()

# Insert games details
for index, row in df_games.iterrows():
    # Create an INSERT statement
    sql = "INSERT INTO games (game_name, developer_name, app_id) VALUES (%s, %s, %s)"
    values = (row['game_name'], row['developer_name'], row['app_id'])
    
    # Execute the SQL command
    cursor.execute(sql, values)

# Commit the changes
db_connection.commit()

# Close the cursor and connection
cursor.close()
db_connection.close()

print("Games table updated successfully.")