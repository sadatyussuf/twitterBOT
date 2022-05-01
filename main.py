import tweepy
from dotenv import load_dotenv
import requests

import os
import logging
import time

load_dotenv()
# logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG,filename="msg.log",filemode='w',
format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s')

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)


#* Create API object
api = tweepy.API(auth,wait_on_rate_limit=True)

#* Authenticate to Twitter
def authenticate():
    if not api.verify_credentials():
        logging.error("Authentication Failed",exc_info=True)
        return False
    else:
        logging.info("Authentication Success!")
        return True


def search_tweets(query,count):
    return  api.search_tweets(q=query,count=count,lang="en",result_type='recent')

def like_tweets(tweets):
    try:
        pass
    except tweepy.TweepError as e:
        pass
def main(query,count=2):
    c = 1
    if authenticate():
        search_resp =search_tweets(query,count)
    
        for tweet in  search_resp:
            print(f"({c}) - {tweet.user.name} with id of {tweet.id} said: {tweet.text} created at : {tweet.created_at}")
            if like_tweets(tweet):
                pass
            print()
            time.sleep(10)
            c+=1




if __name__ == '__main__':
    main('#api')






# url = "https://ghana-shs-api.herokuapp.com/api/shs"
# resp = requests.get(url)

# # print(r.content)

# api_resp = resp.json()

# for i in range(0,5):
#     print(api_resp[i])
#     time.sleep(10)