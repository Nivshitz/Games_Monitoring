-- Create Database
CREATE DATABASE game_monitoring;
USE game_monitoring;

-- Create Games Table
CREATE TABLE games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    game_name VARCHAR(255) NOT NULL,
    developer_name VARCHAR(255) NOT NULL,
    app_id VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Installations Table
CREATE TABLE installations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    date DATE NOT NULL,
    installs INT NOT NULL,
    FOREIGN KEY (game_id) REFERENCES games(game_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Reddit Data 
CREATE TABLE reddit_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    post_title VARCHAR(255),
    post_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (game_id) REFERENCES games(game_id)
);