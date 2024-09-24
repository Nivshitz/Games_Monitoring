<div align="center">

# Game Installation Monitoring & Alert System

</div>

<p align="center">
  <img src="https://github.com/Nivshiz/Games_Monitoring/blob/main/assets/project_workflow.drawio.png" alt="Workflow Diagram" width="600">
</p>

## Overview

This project is part of a final project in a Cloud & Big Data Engineer course at @Naya College.
The project is a Python-based monitoring system designed to track the installation trends of mobile games.
The system uses real-time data from the Google Play Store to monitor installations and identify significant spikes in game popularity.
Alerts are triggered if installation growth exceeds a defined threshold, allowing for timely analysis and decision-making.

The project consists of three core components:
- **Game Data Collection**: Fetches daily installation counts for selected games from the Google Play Store.
- **Trend Analysis**: Monitors installation growth over time, calculating percentage increases.
- **Alert System**: Triggers alerts if a game's installation count shows a significant increase, allowing further analysis.

## Usage
### Prerequisites
- Python 3
- MySQL

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Nivshiz/Games_Monitoring
2. Install the required Python packages:
   ```python
   pip install -r requirements.txt
3. Set up a MySQL database for storing game and installation data. Use [create_game_monitoring_db.sql](/create_game_monitoring_db.sql) file for this.
4. Create a .env file containing your MySQL credentials:
   ```bash
   DB_HOST = your_host
   DB_USER = your_user
   DB_PASSWORD = your_password
   DB_NAME = 'game_monitoring'
6. Add your games to the games table:
   (app_id can be found in the google play url's game page. Just search the game in the google play store)
   ```sql
   INSERT INTO games (name, app_id) VALUES ('Coin Master', 'com.moonactive.coinmaster');
7. Run the script to start monitoring (Daily manually):
   ```python
   python monitor_installations.py

### Configurations (optional):
- **Customize Average Period**:: The script fetches installation counts for all games stored in the games table, calculates the average installs over the last 7 days, and triggers an alert if the increase exceeds the threshold. You can change the number of days calculated in the average.
- **Customize Threshold**: You can change the threshold_percentage in the script to adjust the sensitivity of the alerts.

## Future Work
- **Extract AppStore Data**: Extract and combine installations count from both google play store and apple store.
- **Integrate Reddit Data**: Fetch posts and comments from Reddit for data mining about the game.
- **Integrate OpenAI**: Use GPT to analyze Reddit's data for a deeper understanding of the spikes in the installations count.
- **Cloud Deployment**: Migrate to a cloud-based DB and schedule daily runs using a scheduler service.
- **Visualizations and Analysis**: Use BI tools to create graphs and dashboards for analysts to visualize game trends.
- **Genericize**: Make the system more generic so that the user only needs to select their game, and the system will automatically identify and monitor its competitors.
