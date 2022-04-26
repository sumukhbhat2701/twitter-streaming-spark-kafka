import tweepy
from tweepy import Stream
import socket
import json
import os
from dotenv import load_dotenv
load_dotenv("./creds.env")
 
f = open('hashtags.json')
hashtags = json.load(f)
f.close()

hash_values = [i.lower() for i in list(hashtags.values())]


class MyStreamListener(Stream):
    def set_socket(self, socket):
        self.client_socket = socket
    def on_data(self, data):
        try:
            msg = json.loads(data)
            print( msg['text'].encode('utf-8') )
            self.client_socket.send((str(msg['text']) + "\n").encode('utf-8'))
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


def sendData(c_socket):
    print("HEY", os.getenv('consumer_key'))
    stream = MyStreamListener(os.getenv('consumer_key'), os.getenv('consumer_secret'), os.getenv('access_token'), os.getenv('access_secret'))
    stream.set_socket(c_socket)
    stream.filter(track = hash_values, languages = ["en"])

if __name__ == "__main__":
    s = socket.socket()         
    host = "127.0.0.1"     
    port = 6002          
    s.bind((host, port))        

    print("Listening on port: %s" % str(port))

    s.listen(5)                 
    c, addr = s.accept()        

    print("Received request from: " + str(addr))
    sendData(c)
