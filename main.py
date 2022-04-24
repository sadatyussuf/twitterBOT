import tweepy
from dotenv import load_dotenv

import os

load_dotenv()

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)


#? Create API object
api = tweepy.API(auth,wait_on_rate_limit=True)

# print(api.me())

#? Verify Credentials
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#? Fetch first 20 tweets from Timeline
# timeline = api.home_timeline(count=2)
# for tweet in timeline:
#     print(f'{tweet.user.name} said {tweet.text}')


# Fetch Particular User
user = api.get_user(screen_name="yussufSadat")
print(user.screen_name)
print(user.description)
print(user.location)
print(user.followers_count)


# Search a keyword for most recent public tweets  in english
for tweet in api.search_tweets(q='knust',lang="en",count=5):
    print(f"{tweet.user.name} : {tweet.text}")