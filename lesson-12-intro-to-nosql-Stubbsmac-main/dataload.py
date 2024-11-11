# Import Libraries
from pymongo import MongoClient
import json

# Function to load data into mongo db
def load(client):
    # Import data
    with open('customer.json','r') as file:
        data = json.load(file)

    # Select the database
    db = client['car_rental']

    # Select the collection (table)
    collection = db['customer']

    # Insert the data
    result = collection.insert_many(data)

    # Confirm insertion
    print(f'Insertion of {len(result.inserted_ids)} documents successful')

    # Import data
    with open('car.json','r') as file:
        data = json.load(file)

    # Select the database
    db = client['car_rental']

    # Select the collection (table)
    collection = db['car']

    # Insert the data
    result = collection.insert_many(data)

    # Confirm insertion
    print(f'Insertion of {len(result.inserted_ids)} documents successful')


    # Import data
    with open('rental.json','r') as file:
        data = json.load(file)

    # Select the database
    db = client['car_rental']

    # Select the collection (table)
    collection = db['rental']

    # Insert the data
    result = collection.insert_many(data)

    # Confirm insertion
    print(f'Insertion of {len(result.inserted_ids)} documents successful')

    # Import data
    with open('location.json','r') as file:
        data = json.load(file)

    # Select the database
    db = client['car_rental']

    # Select the collection (table)
    collection = db['location']

    # Insert the data
    result = collection.insert_many(data)

    # Confirm insertion
    print(f'Insertion of {len(result.inserted_ids)} documents successful')