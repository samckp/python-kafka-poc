# python-kafka-poc
#----------------------------------
Produce message in every 5 second

#Kraft mode setup commands  :
1. Generate UUID
./bin/kafka-storage.sh random-uuid

2. format your storage directory (replace <uuid>)
./bin/kafka-storage.sh format -t <uuid> -c config/kraft/server.properties

3. Its ready to start broker in Kraft mode (without zookeeper)
./bin/kafka-server-start.sh config/kraft/server.properties

-----------------------------------