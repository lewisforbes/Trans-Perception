from auth import *
import tweepy
import outputter
import time
import Tweet

q = "\"trans men\" OR \"trans man\" OR \"transgender men\" OR \"transgender man\" OR \"trans women\" OR \"trans woman\" OR \"transgender women\" OR \"transgender woman\""
    
api = get_api_v2()
count = 0
init=True
for resp in tweepy.Paginator(api.search_recent_tweets, q, limit=4000, tweet_fields=["author_id", "created_at", "public_metrics"]):
    count +=1 
    if count%60==0:
        print(count)
        time.sleep(15*60)
    tweets = []
    for t in resp.data:
        metrics = t.public_metrics
        tweets.append(Tweet(t.id, t.created_at, t.text, t.author_id, metrics["like_count"], metrics["retweet_count"]))
    outputter.output(tweets, init)
    init=False

print("Finished")