import sqlite3
import uuid

# Connect to database
conn = sqlite3.connect("btech.db")
cursor = conn.cursor()

# 1. Add a token column if it doesn't already exist
try:
    cursor.execute("ALTER TABLE student_marks ADD COLUMN token TEXT")
    print("Added 'token' column to table.")
except sqlite3.OperationalError:
    print("'token' column already exists.")

# 2. Fetch all unique roll numbers that don't have a token yet
cursor.execute("SELECT DISTINCT roll_no FROM student_marks WHERE token IS NULL OR token = ''")
rolls = cursor.fetchall()

# 3. Generate and assign a unique token for each student
for (roll_no,) in rolls:
    unique_token = uuid.uuid4().hex  # Creates a random 32-character hex string
    cursor.execute("UPDATE student_marks SET token = ? WHERE roll_no = ?", (unique_token, roll_no))
    print(f"Assigned token for roll no: {roll_no}")

conn.commit()
conn.close()
print("Security tokens successfully generated and assigned to students!")