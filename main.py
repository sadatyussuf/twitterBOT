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
    # try:
    #     api.verify_credentials()
    #     logging.info("Authentication Success!")
    #     return True
    # except:
    #     logging.exception("Failed Authentication")
    #     return False
    if not api.verify_credentials():
        logging.error("Authentication Failed",exc_info=True)
        return False
    else:
        logging.info("Authentication Success!")
        return True


def main():
    if authenticate():
        print("do stuff")


if __name__ == '__main__':
    main()






# url = "https://ghana-shs-api.herokuapp.com/api/shs"
# resp = requests.get(url)

# # print(r.content)

# api_resp = resp.json()

# for i in range(0,5):
#     print(api_resp[i])
#     time.sleep(10)