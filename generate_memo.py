import sqlite3
import pandas as pd

# 1. Connect to the SQLite database
conn = sqlite3.connect("btech.db")

# 2. Choose the student roll number to generate for
target_roll = "21A91A0501"

# 3. Query data directly from SQLite using pandas
query = f"SELECT * FROM student_marks WHERE roll_no = '{target_roll}'"
student_data = pd.read_sql(query, con=conn)

conn.close()

if student_data.empty:
    print(f"Student with Roll No {target_roll} not found in the database!")
    exit()

# Extract general info from the first row
name = student_data.iloc[0]["name"]
branch = student_data.iloc[0]["branch"]
semester = student_data.iloc[0]["semester"]

# 4. Build the table rows for subjects
table_rows = ""
total_credits = 0
for _, row in student_data.iterrows():
    total_credits += row["credits"]
    total_marks = row["internal"] + row["external"]
    table_rows += f"""
        <tr>
            <td>{row['subject_code']}</td>
            <td>{row['subject_name']}</td>
            <td>{row['credits']}</td>
            <td>{row['internal']}</td>
            <td>{row['external']}</td>
            <td>{total_marks}</td>
            <td>{row['grade']}</td>
        </tr>
    """

# 5. Create the HTML Template
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>B.Tech Marks Memo - {target_roll}</title>
    <style>
        body {{
            background: #eef2f3;
            font-family: 'Times New Roman', Times, serif;
            margin: 0;
            padding: 30px;
        }}
        .memo-container {{
            max-width: 750px;
            background: #ffffff;
            margin: auto;
            padding: 40px;
            border: 6px double #003366;
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        }}
        .header {{
            text-align: center;
            border-bottom: 2px solid #003366;
            padding-bottom: 15px;
            margin-bottom: 20px;
        }}
        .header h2 {{ margin: 5px 0; color: #003366; font-size: 24px; }}
        .header p {{ margin: 2px 0; color: #555; font-size: 14px; }}
        .student-info {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 20px;
            font-size: 16px;
            background: #f9f9f9;
            padding: 15px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }}
        th, td {{
            border: 1px solid #999;
            padding: 10px;
            text-align: center;
            font-size: 14px;
        }}
        th {{
            background-color: #003366;
            color: white;
        }}
        .summary {{
            font-size: 16px;
            margin-bottom: 30px;
            font-weight: bold;
        }}
        .footer {{
            display: flex;
            justify-content: space-between;
            margin-top: 50px;
            font-size: 14px;
            font-weight: bold;
            border-top: 1px dashed #999;
            padding-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="memo-container">
        <div class="header">
            <h2>JAWAHARLAL TECHNOLOGICAL UNIVERSITY</h2>
            <p>B.Tech Semester Examination Marks Memo</p>
        </div>
        
        <div class="student-info">
            <div><strong>Student Name:</strong> {name}</div>
            <div><strong>Roll Number:</strong> {target_roll}</div>
            <div><strong>Branch:</strong> {branch}</div>
            <div><strong>Semester:</strong> {semester}</div>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Subject Code</th>
                    <th>Subject Name</th>
                    <th>Credits</th>
                    <th>Internal</th>
                    <th>External</th>
                    <th>Total (100)</th>
                    <th>Grade</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>

        <div class="summary">
            <p>Total Credits Registered: {total_credits}</p>
            <p>Status: PASSED</p>
        </div>

        <div class="footer">
            <div>Date of Issue: October 2026</div>
            <div>Controller of Examinations</div>
        </div>
    </div>
</body>
</html>
"""

# 6. Save output to an HTML file
output_filename = f"memo_{target_roll}.html"
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated marks memo from SQLite Database! Open '{output_filename}' in your browser.")