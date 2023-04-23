from time import sleep
from json import dumps
from kafka import KafkaProducer

topic_name='test-topic'
producer = KafkaProducer(bootstrap_servers=['172.29.192.1:9092'], value_serializer=lambda x:
dumps(x).encode('utf-8'))

for e in range(10):
    data = {'number' : e}
    print(data)
    producer.send(topic_name, value=data)
    sleep(0.005)
