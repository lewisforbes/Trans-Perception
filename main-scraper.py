from auth import *
import tweepy
import outputter
import time
import Tweet

def tweets_so_far():
    with open("raw_results.csv", 'r', encoding="utf-8") as fp:
        for i, v in enumerate(fp):
            pass
    return i


def go(init, goal):
    q = "(\"trans men\" OR \"trans man\" OR \"transgender men\" OR \"transgender man\" OR \"trans women\" OR \"trans woman\" OR \"transgender women\" OR \"transgender woman\") -is:retweet"
    api = get_api_v2()
    count = 0
    for resp in tweepy.Paginator(api.search_recent_tweets, q, tweet_fields=["author_id", "created_at", "public_metrics"], sort_order="recency", max_results=100):
        count+=1
        if count%50==0:
            tsf=tweets_so_far()
            if tsf>=goal:
                return
            print("tweets so far: {}/{}".format(tsf, goal))
            time.sleep(15*60) # rate limit 
        tweets = []
        for t in resp.data:
            metrics = t.public_metrics
            tweets.append(Tweet.Tweet(t.id, t.created_at, t.text, t.author_id, metrics["like_count"], metrics["retweet_count"]))
        outputter.output(tweets, init)
        init=False
    print("returned")
    return
    

print("start")
goal=30000
init=True
while init or tweets_so_far()<goal:
    try:
        go(init, goal)
        init=False
    except:
        print("error") # API unavailable at this tier (not personal rate limit)
        time.sleep(5*60)
print("Finished")
