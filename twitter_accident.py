import tweepy
from bearer_token import tok_name 

bearer_token=(tok_name)


client = tweepy.Client(bearer_token=bearer_token)

# Replace with your own search query

#IF we Search Injuries on twitter Then plese uncommit on 13 line and commit 15 line

# query = 'injuries -is:retweet'

query = 'accident -is:retweet'

list_of_location = []
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                     user_fields=['location'], expansions='author_id', max_results=100)


# Get users list from the includes object
users = {u["id"]: u for u in tweets.includes['users']}

for tweet in tweets.data:
    if users[tweet.author_id]:
        
        user = users[tweet.author_id]
        us1 = dict(user)
        
        list_of_location.append(user.location)

print(list_of_location)


