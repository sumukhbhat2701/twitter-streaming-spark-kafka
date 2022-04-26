from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaConsumer
import json
import pymongo
from pymongo import MongoClient
import pprint

 
f = open('hashtags.json')
 
hashtags = json.load(f)

f.close()

hash_values = [i.lower() for i in list(hashtags.values())]

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092", 
    client_id='test'
)

topic_list = []

my_topics = admin_client.list_topics()
for i in hash_values:
    if i not in my_topics:
        topic_list.append(NewTopic(name=i, num_partitions=1, replication_factor=1))

admin_client.create_topics(new_topics=topic_list, validate_only=False)

if __name__ == '__main__':
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client['dbt_assignment']
    collection = db['stream_twitter']

    consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
    consumer.subscribe(topics = tuple(hash_values))
    for message in consumer:
        res = message.value.decode('utf8')
        print(res)

        l = res.split(";")
        d = {}
        d["Hashtag"] = l[0]
        d["Count"] = l[1]
        d["Timestamp"] = l[2]

        collection.insert_one(d)
        
        print("# Documents = ",  collection.find().count())
        for data in collection.find():
            pprint.pprint(data)

        print("-"*60)

