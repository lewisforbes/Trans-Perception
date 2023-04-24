import tweepy

# creds.txt
# consumer key=.....
# consumer secret=.....
# access token=.....
# access token secret=.....
# bearer token=.....

def get_creds(filename="creds.txt"):
    f = open("creds.txt", "r")
    creds = []
    for line in f:
            if len(line)<5: # skip last line if empty
                continue
            creds.append(line.split("=")[1].strip())
    return creds


def get_api_v1():
    consumer_key, consumer_secret, access_token, access_token_secret, bearer_token = get_creds()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create the API object
    api = tweepy.API(auth)
    return api

def get_api_v2():
    consumer_key, consumer_secret, access_token, access_token_secret, bearer_token = get_creds()
    client = tweepy.Client(bearer_token=bearer_token)
    return client