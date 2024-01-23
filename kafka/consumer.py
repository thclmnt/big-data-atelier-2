from kafka import KafkaConsumer

TOPIC = 'bike_station_data'
CONSUMER = KafkaConsumer(TOPIC,bootstrap_servers='localhost:9092', enable_auto_commit=False)

try:
    for message in CONSUMER:
        key = message['key'].decode('utf-8')
        data = message['value'].decode('utf-8')

        print(f"Clé: {key}, Data: {data}")
        CONSUMER.commit()
except:
    pass