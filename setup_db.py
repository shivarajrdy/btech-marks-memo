import sqlite3

# This automatically creates a local database file named 'btech.db' in your folder
db = sqlite3.connect("btech.db")
cursor = db.cursor()

# 1. Create the student marks table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_marks (
        roll_no TEXT,
        name TEXT,
        branch TEXT,
        semester INTEGER,
        subject_code TEXT,
        subject_name TEXT,
        credits INTEGER,
        internal INTEGER,
        external INTEGER,
        grade TEXT
    )
""")
print("SQLite Table 'student_marks' created successfully!")

# 2. Check if sample data already exists
cursor.execute("SELECT COUNT(*) FROM student_marks")
count = cursor.fetchone()[0]

if count == 0:
    sample_data = [
        ("21A91A0501", "Rahul Sharma", "CSE", 4, "CS401", "Data Structures", 4, 22, 58, "A"),
        ("21A91A0501", "Rahul Sharma", "CSE", 4, "CS402", "Operating Systems", 3, 20, 55, "B+"),
        ("21A91A0501", "Rahul Sharma", "CSE", 4, "CS403", "Database Management", 4, 24, 62, "A+"),
        ("21A91A0501", "Rahul Sharma", "CSE", 4, "CS404", "Computer Networks", 3, 19, 50, "B")
    ]
    cursor.executemany("""
        INSERT INTO student_marks (roll_no, name, branch, semester, subject_code, subject_name, credits, internal, external, grade)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, sample_data)
    db.commit()
    print("Sample student data inserted successfully into SQLite!")

db.close()

