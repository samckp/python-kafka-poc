start cmd /k F:/kafka_2.13-3.5.0/bin/windows/zookeeper-server-start.bat F:/kafka_2.13-3.5.0/config/zookeeper.properties
pause

start cmd /k F:/kafka_2.13-3.5.0/bin/windows/kafka-server-start.bat F:/kafka_2.13-3.5.0/config/server.properties


