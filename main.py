import tweepy

CONSUMER_KEY = "R7DtIMMSlEBfcaU8h5wX812il"
CONSUMER_SECRET = "gOZKbDg7WLl5vLj9cqAqR3EBnPvRIrkJmRjEZqseovfZCZkYsC"
ACCESS_TOKEN = "784007214503723008-CCxhAJh38jvGgMce33Tid8dHp6iDKkP"
ACCESS_SECRET = "zWRr1yPzooOnHvRiRhc0f2vWrD2ZhTtL6t7VXotTmgDwF"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAANSIbgEAAAAAQJj29L%2FmHvyh0ftH1yqfQOBLIYQ%3DuvHsSqibTd9NibMpYNniyVQrLLeGHolkZURQXhitOKINmT4gRH"


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

#? Create a tweet
# api.update_status("Hello World from Tweepy Python")


# Fetch Particular User
user = api.get_user(screen_name="twitter")
print(user.screen_name)
print(user.description)
print(user.location)
print(user.followers_count)