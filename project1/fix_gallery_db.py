import sqlite3

db_path = 'db.sqlite3'

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("Checking authapp_gallery columns...")
    cursor.execute("PRAGMA table_info(authapp_gallery)")
    columns = [info[1] for info in cursor.fetchall()]
    print(f"Columns: {columns}")
    
    if 'timeStamp' not in columns:
        print("Adding 'timeStamp'...")
        cursor.execute("ALTER TABLE authapp_gallery ADD COLUMN timeStamp datetime DEFAULT '2025-01-01 00:00:00'")
        conn.commit()
        print("Column added.")
    else:
        print("Column already exists.")
        
    conn.close()

except Exception as e:
    print(f"Error: {e}")
