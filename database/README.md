# Database Module - `database`

This module provides functionality for interacting with a SQLite database to store and retrieve circular object data detected in images.

## Contents

- `__init__.py`: Exports the `circle_database` instance
- `helper.py`: Contains the `CircleDatabase` class implementation

## Key Components

### CircleDatabase Class

The `CircleDatabase` class manages connections to the SQLite database and provides methods for storing and retrieving circular object data.

#### Methods

- `__init__()`: Initializes the database connection
- `connect()`: Establishes a connection to the database
- `close()`: Closes the database connection
- `__enter__()` and `__exit__()`: Allows usage of the class with context managers
- `_create_table()`: Creates the `circular_objects` table if it doesn't exist
- `store_circle_data(image_name, circle_count, metadata)`: Stores or updates circle data for an image
- `get_circle_data_db(image_name)`: Retrieves circle data for a specific image

### Global Instance

- `circle_database`: A global instance of the `CircleDatabase` class, created at the end of `helper.py`

## Usage

```python
from database import circle_database

# Storing data
image_name = "example.jpg"
circle_count = 5
metadata = [{"circle_id": 1, "center": (100, 100), "radius": 50}, ...]
circle_database.store_circle_data(image_name, circle_count, metadata)

# Retrieving data
data = circle_database.get_circle_data_db(image_name)
if data:
    count, metadata = data
    print(f"Circles found: {count}")
    print(f"Metadata: {metadata}")
```

## Database Structure

The `circular_objects` table has the following schema:
- `image_name` (TEXT): Primary key, name of the image file
- `circle_count` (INTEGER): Number of circles detected in the image
- `metadata` (TEXT): JSON string containing detailed information about each detected circle

## Error Handling

- The module uses extensive error handling and logging for database operations.
- Errors are logged using a custom logger (`custom_logger.logger`).
- Most database errors are caught and re-raised, allowing for proper error handling in the calling code.

## Configuration

- The database path is imported from the `utilities` module as `DATABASE_PATH`.
- Ensure that the `DATABASE_PATH` is correctly set in the `utilities` module before using this database module.

## Notes

- The database connection is set up to be thread-safe (`check_same_thread=False`).
- The module uses context managers for proper resource management.
- Make sure to close the database connection when it's no longer needed, or use the class with a context manager.