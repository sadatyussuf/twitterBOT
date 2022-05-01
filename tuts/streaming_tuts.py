import tweepy
import json

class MyStreamListener(tweepy.Stream):
    def __init__(self,api):
        # super().__init__(consumer_key, consumer_secret, access_token, access_token_secret, **kwargs)
        self.api = api
        self.me = api.me()
    
    def on_status(self,tweet):
        print(f"{tweet.user.name} : {tweet.text}")
    def on_error(self,status):
        print("Error detected")
# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])

