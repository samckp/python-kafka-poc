from kafka import KafkaProducer
import json
import threading

#Brokers list
bootstrap_servers = ['localhost:9092']
topic = 'mytopic'

#bulk messages 
bulk_msgs = [
    {'id': i, 'name': f'User {i}'} for i in range(100000)
]

producer_config = {
    'bootstrap_servers' : bootstrap_servers,
    'acks': 0,
    'compression_type': 'gzip',
    'batch_size': 16384,
    'linger_ms': 0,
    'max_request_size': 1048576,
    'buffer_memory': 67108864
}

#function to push messages 

def push_messages(messages):

    producer = KafkaProducer(**producer_config)

    for msg in messages:
        producer.send(topic, json.dumps(msg).encode('utf-8'))

    producer.flush()

    producer.close()


batch_size = 16384
for i in range(0, len(bulk_msgs), batch_size):
    batch = bulk_msgs[i:i+batch_size]
    thread = threading.Thread(target=push_messages, args=(batch,) )
    thread.start()

