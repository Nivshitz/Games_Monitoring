from db_connector import game_monitoring_connector
from update_installations_table import update_installations_table
from p_chg_plotting import p_chg_plot
from monitor_installations import monitor_installations

if __name__ == '__main__':
    db_connection = game_monitoring_connector()
    cursor = db_connection.cursor()

    update_installations_table(cursor)
    # Commit the installations_table changes
    db_connection.commit()

    # Monitor the game installations
    monitor_installations(cursor)

    # Plot percentage change over time
    p_chg_plot(cursor)

    # Close the cursor and the db connection
    cursor.close()
    db_connection.close()