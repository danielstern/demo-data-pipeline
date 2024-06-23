# Data Pipeline Simulator

## Description
A simple application simulating a real-time data pipeline.

## Running the App
1. Start the server with `python3 server.py`
2. Start simulating data with `python3 simulator.py`. A new file will be created every 10 seconds until this method is stopped.

## Challenge Activities
1. Can you change the storage medium from the `tmp/` folder to a Postgres database running locally?
2. Can you update the simulator to add a randomly generated first  and last name - and then update the data cleaner to mask or bucket that information?
3. Can you containerize the server and get it running on the cloud? (Beware cloud expenses.)
4. Can you change the storage medium again from a local database to a cloud native database running remotely? (e.g., AWS DynamoDB). Once again, be aware of any expenses you will incur, and delete the cloud resources once you are done this exercise.