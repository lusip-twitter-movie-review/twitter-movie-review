from slistener import SListener
import time, tweepy, sys
import traceback
import json
# #Consumer Keys and access tokens, used for OAuth
cred_file = open("cred.json")
cred = json.load(cred_file)
consumer_key = cred[0]
consumer_secret = cred[1]
access_token = cred[2]
access_token_secret = cred[3]

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def main():
    track = ['The Shallows']
 
    listen = SListener(api, 'movie_data')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track, languages=["en"])
    except Exception as e:
        print traceback.print_exc()
        stream.disconnect()

if __name__ == '__main__':
    main()
