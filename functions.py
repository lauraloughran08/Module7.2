import csv
from datetime import datetime  # Add this line to import datetime module

def write_to_csv(events, file_path):
    # Sort events based on timestamps
    sorted_events = sorted(events, key=lambda x: datetime.strptime(x['timestamp'], "%Y-%m-%d %H:%M:%S"))

    # Write to CSV file
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Event', 'Timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for event in sorted_events:
            writer.writerow({'Event': event['event'], 'Timestamp': event['timestamp']})


def read_and_display_csv(file_path):
    # Read from CSV file
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        events = list(reader)

    return events

