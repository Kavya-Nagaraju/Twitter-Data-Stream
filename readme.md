## Twitter Data Stream
Stream Covid-19 related Twitter Data into BigQuery, using Pub/Sub.
</br>
![Alt text](design.jpg?raw=true)
</br>
The project demonstartes, developement of ETL pipeline on GCP.
 EXTRACT - Stream data from Twitter.
 TRANSFORM - Parse required fields from invidual tweets. 
 LOAD - Load data to Pub/Sub topic which is collected in a Big Query Table.

#### Requirements for the task are:

1. Twitter Developer account
2. Google Cloud Platform account

#### Main steps of process are:

1. Obtaining Twitter credentials
2. Create IAM Service accound and assigned following roles.
- BigQuery Data Editor
- BigQuery Job User
- Dataflow Developer
- Pub/Sub Editor

##### Creating a Producer
    PRODUCER - Listen to streaming Twitter data, I have used tweepy library that takes an Array of keywords that will filter the real-time tweet stream. Upon receiving the data, the data is published to `tweets` topic of the Pub/Sub model.

##### Creating a Consumer
    CONSUMER - Consumer is a Cloud Data Flow job. Consumer’s task is to stream messages from Pub/Sub topic `tweets` to BigQuery table. A Big Query table is created with the below schema.
    created_at :	STRING		
    id :	STRING		
    retweet_count :	STRING		
    text :	STRING		
    user_name :	STRING		
    user_location :	STRING		
    user_followers_count :	STRING		

##### The collected data has the below USECASES:
 1. Determine total tweets, for each hour, day, week etc.
 2. Determine total tweets for each region.

 This information can be used to find crisis.

 ##### Future Work
 1. Perform sentiment analysis of tweets.
 2. Docekrize producer and run it from GCP for end-to-end execution of ETL pipeline on GCP.
 3. Connect the big query table to sophisticated visulization tools, to perform real-time visualizations on the streaming data.