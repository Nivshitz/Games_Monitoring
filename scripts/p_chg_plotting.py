import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def p_chg_plot(cursor):
    query = """
        SELECT game_name, date, installs 
        FROM installations
        INNER JOIN games
                ON installations.game_id = games.game_id
        ORDER BY date ASC
    """
    cursor.execute(query)
    data = cursor.fetchall()

    df = pd.DataFrame(data = data, columns=['game_name', 'date', 'installsCount'])

    # Convert 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    games = df['game_name'].unique()
    colors = ['blue', 'green', 'red', 'orange', 'purple']

    # Calculate percentage change for each game
    df['percentage_change'] = df.groupby('game_name')['installsCount'].pct_change() * 100

    # Create subplots
    fig, axes = plt.subplots(nrows=len(games), ncols=1, figsize=(10, 12), sharex=True)

    # Plot each game on a separate subplot
    for i, game_name in enumerate(games):
        game_data = df[df['game_name'] == game_name]
        axes[i].plot(game_data['date'], game_data['percentage_change'], marker='o', color=colors[i])
        axes[i].set_title(f'{game_name} Percentage Change in Installations Over Time', fontsize=12)
        axes[i].set_ylabel('Percentage Change (%)')
        axes[i].grid(True)

        # Format the date as 'dd/mm/yyyy'
        axes[i].xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))

    plt.xlabel('Date')
    plt.tight_layout() # Adjust layout to avoid overlapping

    plt.show()
