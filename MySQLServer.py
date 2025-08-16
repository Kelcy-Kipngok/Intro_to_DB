#!/usr/bin/python3
"""
Script to create the database alx_book_store
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update with your credentials if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error: Could not connect to MySQL server\n{e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed") # optional

if __name__ == "__main__":
    create_database()
