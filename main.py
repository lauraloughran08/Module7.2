# Laura Loughran
# November 26, 2023
# Module 7 practice 2

from app.functions import write_to_csv, read_and_display_csv

# Sample events
events = [
    {"event": "login", "timestamp": "2023-10-15 08:10:05"},
    {"event": "logout", "timestamp": "2023-10-15 10:12:40"},
    {"event": "login", "timestamp": "2023-10-15 11:05:10"}
]

# File path for CSV
csv_file_path = 'events_log.csv'

# Write events to CSV
write_to_csv(events, csv_file_path)

# Read and display events from CSV
read_and_display_csv(csv_file_path)
