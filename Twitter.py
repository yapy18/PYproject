import tweepy
import config


client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

#consumer_key=config.api_key,
#consumer_secret=config.api_secret,
#access_token=config.access_token,
#access_secret=config.access_secret,

query = 'kill,;retweet'

file_name = 'tweets.txt'

with open(file_name, 'a+') as filehandler:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,max_results=100,).flatten(limit=1000):
        print(tweet.id)
        filehandler.write('%s\n' % tweet.id)



