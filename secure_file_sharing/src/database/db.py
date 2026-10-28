import sqlite3


from src.config import DB_FILE
from src.utils.logger import logger


def get_connection():
    #check_same_thread is needed because we might handle request on different threads later
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)

    conn.row_factory=sqlite3.Row
    return conn



def init_db():
    logger.info("Initializing databse schema...")
    conn=get_connection()
    cursor= conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )            
""")

        # 2. Create the Files table (with a Foreign Key linking to users)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                internal_filename TEXT UNIQUE NOT NULL,
                owner_id INTEGER NOT NULL,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (owner_id) REFERENCES users (id)
            )
        """)

        conn.commit()
        logger.info("Database table created successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}", exc_info=True)
    finally:
        conn.close()

