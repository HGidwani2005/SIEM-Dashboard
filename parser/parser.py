import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Clear old logs to avoid duplicates
cursor.execute("DELETE FROM logs")

with open("logs/auth.log", "r") as file:
    for line in file:
        log = line.strip()

        parts = log.split()

        timestamp = " ".join(parts[:3])
        service = parts[3]
        message = " ".join(parts[4:])

        cursor.execute(
            "INSERT INTO logs(timestamp, service, message) VALUES (?, ?, ?)",
            (timestamp, service, message)
        )

conn.commit()
conn.close()

print("Logs inserted successfully!")