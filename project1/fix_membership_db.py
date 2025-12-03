import sqlite3

db_path = 'db.sqlite3'

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("Checking authapp_membershipplan columns...")
    cursor.execute("PRAGMA table_info(authapp_membershipplan)")
    columns = [info[1] for info in cursor.fetchall()]
    print(f"Columns: {columns}")
    
    if 'description' not in columns:
        print("Adding 'description'...")
        cursor.execute("ALTER TABLE authapp_membershipplan ADD COLUMN description TEXT DEFAULT ''")
    
    if 'duration_days' not in columns:
        print("Adding 'duration_days'...")
        cursor.execute("ALTER TABLE authapp_membershipplan ADD COLUMN duration_days INTEGER DEFAULT 30")
        
    if 'is_active' not in columns:
        print("Adding 'is_active'...")
        cursor.execute("ALTER TABLE authapp_membershipplan ADD COLUMN is_active BOOLEAN DEFAULT 1")
        
    if 'created_at' not in columns:
        print("Adding 'created_at'...")
        cursor.execute("ALTER TABLE authapp_membershipplan ADD COLUMN created_at datetime DEFAULT '2025-01-01 00:00:00'")
        
    if 'updated_at' not in columns:
        print("Adding 'updated_at'...")
        cursor.execute("ALTER TABLE authapp_membershipplan ADD COLUMN updated_at datetime DEFAULT '2025-01-01 00:00:00'")
        
    conn.commit()
    print("Done.")
    conn.close()

except Exception as e:
    print(f"Error: {e}")
