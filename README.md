# Game Installation Monitoring & Alert System

## Overview

This project is a Python-based monitoring system designed to track the installation trends of mobile games. The system uses real-time data from the Google Play Store to monitor installations and identify significant spikes or trends in game popularity. Alerts are triggered if installation growth exceeds a defined threshold, allowing for timely analysis and decision-making.

The project consists of three core components:
1. **Game Data Collection**: Fetches daily installation counts for selected games from the Google Play Store.
2. **Trend Analysis**: Monitors installation growth over time, calculating percentage increases.
3. **Alert System**: Triggers alerts if a game's installation count shows a significant increase, allowing further investigation.

## Features

- **Automated Data Collection**: Fetches installation data for multiple games daily using the Google Play Scraper API.
- **Trend Analysis**: Calculates average percentage increases over a customizable period (e.g., 7 days).
- **Alerts**: Generates alerts when installation growth exceeds the set threshold.
- **Data Storage**: Uses MySQL to store game and installation data.
- **Scalable**: The system automatically adjusts to new games and scales with more data points.

## Getting Started

### Prerequisites

To run the project locally, you’ll need:

- **Python 3.x**
- **MySQL** (local or cloud)
- **Google Play Scraper** (`google-play-scraper` package)
- **Git** for version control
- **MySQL Connector** for Python

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git