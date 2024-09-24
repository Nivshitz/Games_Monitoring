from db_connector import game_monitoring_connector
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def p_chg_plot():
    db_connection = game_monitoring_connector()

    # Query the installations table
    query = """
        SELECT game_name, date, installs 
        FROM installations
        INNER JOIN games
                ON installations.game_id = games.game_id
        ORDER BY date ASC
    """
    cursor = db_connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    # Close the database connection
    db_connection.close()

    df = pd.DataFrame(data = data, columns=['game_name', 'date', 'installsCount'])

    print(df)

    # Convert 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Create a list of unique game names
    games = df['game_name'].unique()

    # Calculate percentage change for each game
    df['percentage_change'] = df.groupby('game_name')['installsCount'].pct_change() * 100
    print(df)
    # Colors for each game
    colors = ['blue', 'green', 'red', 'orange', 'purple']

    # Create subplots (5 rows, 1 column)
    fig, axes = plt.subplots(nrows=len(games), ncols=1, figsize=(10, 12), sharex=True)

    # Plot each game on a separate subplot
    for i, game_name in enumerate(games):
        game_data = df[df['game_name'] == game_name]
        axes[i].plot(game_data['date'], game_data['percentage_change'], marker='o', color=colors[i])
        axes[i].set_title(f'{game_name} Percentage Change in Installations Over Time', fontsize=12)
        axes[i].set_ylabel('Percentage Change (%)')
        axes[i].grid(True)

        # Format the date as dd/mm/yyyy
        axes[i].xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))

    # Set common labels
    plt.xlabel('Date')
    plt.tight_layout()  # Adjust layout to avoid overlapping

    # Display the plot
    plt.show()

if __name__ == '__main__':
    p_chg_plot()