-- Create database if not exists
CREATE DATABASE IF NOT EXISTS webappdb;

-- Use the database
USE webappdb;

-- Create transactions table
CREATE TABLE IF NOT EXISTS transactions (
    id INT NOT NULL AUTO_INCREMENT,
    amount DECIMAL(10,2),
    description VARCHAR(100),
    PRIMARY KEY(id)
);

-- Insert sample data
INSERT INTO transactions (amount, description) VALUES 
    ('400.00', 'groceries'),
    ('150.50', 'utilities'),
    ('75.25', 'transportation');

-- Grant privileges (optional, for additional security)
FLUSH PRIVILEGES;
