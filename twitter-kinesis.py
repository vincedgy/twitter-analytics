''' '''

import twitterCreds
import twitter
import boto3
import json

## twitter credentials
consumer_key = twitterCreds.consumer_key
consumer_secret = twitterCreds.consumer_secret
access_token_key = twitterCreds.access_token_key
access_token_secret = twitterCreds.access_token_secret

api = twitter.Api(  consumer_key=consumer_key,
                    consumer_secret=consumer_secret, 
                    access_token_key=access_token_key, 
                    access_token_secret=access_token_secret)

