# twitter-streaming-spark-kafka
Stream twitter data using Spark and Kafka based on hashtags

- (Download and) Run Zookeeper server using `zookeeper-server-start.sh config/zookeeper.properties`
- (Download and) Run Kafka broker server using `bin/kafka-server-start.sh config/server.properties`
- Run stream_tweets.py using `python3 stream_tweets.py`
- Run kafka-consumer.py using `kafka-consumer.py`
- (Download Spark and) Execute the notebook : spark-streaming.ipynb
