from src.database.db import get_connection

def runtest():

    conn=get_connection()

    cursor=conn.cursor()

    try:    

        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                    ("admin", "fakehash123")        
                ) 

        conn.commit()
        print("Success! User 'admin' saved to the database.")

        cursor.execute("SELECT * FROM users")

        rows= cursor.fetchall()

        print("\nCurrent Users in Database:")

        for row in rows:
                    print(f" - ID: {row['id']} | Username:{row['username']} | Created: {row['created_at']}") 


    except Exception as e:
        print(f"Database error: {e}")

    finally: 
          conn.close()


if __name__=="__main__":
      runtest()
