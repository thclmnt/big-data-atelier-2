import time
import json
import requests
from kafka import KafkaProducer

SERVER_URL = 'localhost:3000/api/data'

PRODUCER = KafkaProducer(bootstrap_servers='localhost:9092')
TOPIC = 'bike_station_data'

def get_data(page_number):
    r = requests.get(f'{SERVER_URL}?page={page_number}')
    return r.json()

def create_message(data):
    key = str(data["station_id"])
    PRODUCER.send(TOPIC, key=key.encode(), value=json.dumps(data).encode())
    return

page = 0
while True:
    try:
        data = get_data(page)
        if data == []:
            break

        create_message(data)

        page += 1
        time.sleep(1)

    except:
        pass