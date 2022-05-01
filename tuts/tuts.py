from ast import Pass
import tweepy
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
user = api.get_user(screen_name="twitter")
print(user.screen_name)
print(user.description)
print(user.location)
print(user.followers_count)

# Fetch a number of Followers
for follower in user.followers():
    print(follower.name)

#  Create a tweet
api.update_status("Hello World from Tweepy Python")


# Follow a users
api.create_friendship(screen_name="realpython")

# Change profile description
api.update_profile(description="I like Python")

# Like most recent tweet in timeline
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(id=tweet.id)


# Fetch block User
for block in api.block():
    print(block.name)


# Search a keyword for most recent public tweets  in english
for tweet in api.search(q='Python',lang="en",rpp=10):
    print(f"{tweet.user.name} : {tweet.text}")


# Fetch a list of trending topics
trends_result = api.get_place_trends(1)
for trend in trends_result[0]["trend"]:
    print(trend["name"])



# Fetch tweets user is mentioned in, like the tweet and folllow the user that mentioned you.
tweets = api.mentions_timeline()
for tweet in tweets:
    tweet.create_favorite()
    tweet.user.follow()


# Using Cursor to Fetch more than the first page of the API
for tweet in tweepy.Cursor(api.home_timeline).items(100):
    print(f"{tweet.user.name} said: {tweet.text}")