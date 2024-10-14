# Path Libraries
import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import sqlite3
import json
from config import DATABASE_PATH

from custom_logger import logger

class CircleDatabase:
    def __init__(self):
        self.db_path = DATABASE_PATH
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        if not self.conn:
            try:
                self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
                self.cursor = self.conn.cursor()
                self._create_table()
                logger.info(f"Connected to database: {self.db_path}")
            except sqlite3.Error as e:
                logger.error(f"Error connecting to database: {e}")
                raise

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
            logger.info("Database connection closed")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def _create_table(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS circular_objects (
                    image_name TEXT PRIMARY KEY,
                    circle_count INTEGER,
                    metadata TEXT
                )
            ''')
            self.conn.commit()
            logger.info("Circular objects table created or already exists")
        except sqlite3.Error as e:
            logger.error(f"Error creating table: {e}")
            raise

    def store_circle_data(self, image_name, circle_count, metadata):
        self.connect()
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO circular_objects (image_name, circle_count, metadata) 
                VALUES (?, ?, ?)
            ''', (image_name, circle_count, json.dumps(metadata)))
            self.conn.commit()
            logger.info(f"Stored circle data for image: {image_name}")
        except sqlite3.Error as e:
            logger.error(f"Error storing circle data for image {image_name}: {e}")
            raise

    def get_circle_data_db(self, image_name):
        self.connect()
        try:
            self.cursor.execute("SELECT circle_count, metadata FROM circular_objects WHERE image_name = ?", (image_name,))
            data = self.cursor.fetchone()
            if data:
                logger.info(f"Retrieved circle data for image: {image_name}")
            else:
                logger.warning(f"No circle data found for image: {image_name}")
            return data
        except sqlite3.Error as e:
            logger.error(f"Error retrieving circle data for image {image_name}: {e}")
            raise

circle_database = CircleDatabase()