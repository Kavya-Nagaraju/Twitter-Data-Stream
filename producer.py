import json
from tweepy import Stream
from tweepy.streaming import Stream
from google.cloud import pubsub_v1

# Create Twittter Application on Twitter Developer account and fill the below values.
TWITTER_CONSUMER_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXX"
TWITTER_CONSUMER_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXX"
TWITTER_ACCESS_TOKEN= "XXXXXXXXXXXXXXXXXXXXXXXXX"
TWITTER_ACCESS_TOKEN_SECRET= "XXXXXXXXXXXXXXXXXXXXXXXXX"

# Get Googel Authentication credentials from IAM for the application on Google Cloud Platform account 
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/path/to/downloaded/google-credentials-json-file"

project_id = "propane-highway-326820"
topic_id = "tweets"

# Create publisher to publish data to GCP PUB/SUB
client = pubsub_v1.PublisherClient()
topic_path = client.topic_path(project_id, topic_id)

# Implement TwitterStream Api Listener
class listener(Stream):
    def on_data(self, data):     
        my_dict = json.loads(data)
        transformed_data = dict()
        transformed_data['created_at'] = my_dict['created_at']
        transformed_data['id'] = my_dict['id_str']
        transformed_data['retweet_count'] = my_dict['retweet_count']
        transformed_data['text'] = my_dict['text']
        transformed_data['user_name'] = my_dict['user']['name']
        transformed_data['user_location'] = my_dict['user']['location']
        transformed_data['user_followers_count'] = my_dict['user']['followers_count']

        # print(transformed_data)
        client.publish(topic_path, data= json.dumps(transformed_data).encode('utf-8'))
        return True

    def on_error(self, status):
        print(status)

twitterStream = listener(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET )

# Extract data related to particular track
twitterStream.filter(track=["#Covid19", "#Covid"], languages=['en'], stall_warnings=True)
