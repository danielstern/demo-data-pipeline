import random
import urllib.request
import json
from datetime import datetime, timedelta

def get_message():
    units_completed = random.randint(0, 5)  # Adjusted to ensure units are non-negative
    locations = ["New York", "Sydney", None, "Luxembourg", "Toronto", "San Francisco"]
    location = random.choice(locations)
    date = datetime.now().isoformat()  # Convert datetime to ISO 8601 string
    return { 'units': units_completed, 'location': location, 'date': date }

def daemon():
    message = get_message()
    body = json.dumps(message).encode('utf-8')  # Encode message as JSON bytes
    post("http://localhost:8080", body)

# Assuming a simplified version of set_interval
def set_interval(func, interval):
    while True:
        func()
        datetime_now = datetime.now()
        datetime_next = datetime_now + timedelta(milliseconds=interval)
        while datetime_now < datetime_next:
            datetime_now = datetime.now()

# Define a function to simulate posting data using URLLib
def post(url, data):
    try:
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                print("Data sent successfully")
            else:
                print(f"Failed to send data. Status code: {response.getcode()}")
    except urllib.error.URLError as e:
        print(f"Error sending data: {e}")

# Start the daemon with an interval of 4000 milliseconds (4 seconds)
set_interval(daemon, 4000)
