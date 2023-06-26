from json import loads
from kafka import KafkaConsumer

#Brokers list
bootstrap_servers = ['localhost:9092']
topic = 'mytopic'

consumer_config = {    
    
    'bootstrap_servers' : bootstrap_servers,
    'auto_offset_reset' : 'earliest',
    'enable_auto_commit'  : False,
    'group_id' :'my-group'
}
consumer = KafkaConsumer(topic, **consumer_config,  value_deserializer=lambda x: loads(x.decode('utf-8')))
 
for message in consumer:   
    print ("%s: partition = %d : offset = %d: value= %s" % (message.topic, message.partition,
                                          message.offset, message.value))
    
# consumer.subscribe(pattern='^topic.*')

# for message in consumer:   
    # print ("%s: partition = %d : offset = %d: value= %s" % (message.topic, message.partition,
                                        #   message.offset, message.value))
    
