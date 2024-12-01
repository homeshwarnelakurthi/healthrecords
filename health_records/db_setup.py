import mysql.connector
import bcrypt

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Homesh@99",
    "database": "secure_health_db"
}

def initialize_database():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Create health_info table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS health_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            gender BOOLEAN,
            age INT,
            weight FLOAT,
            height FLOAT,
            health_history TEXT
        )
    """)

   
