import tweepy
from time import sleep
consumer_key='AVufxP0DqrT4sTbngqUaKTwjL'
consumer_secret='NOjUrcsmImkqEON8qQ31dc3I2JHgmVfyL0zzzjImeK40MmIH6T'
access_token='1354042802-bmzvxFiCchmtMxi3rrgK9Tadz588IWip4FojxnB'
access_token_secret='kc1D9r5CQ2gSaOzSfMnpXjMoPZrnuRiEmvkOVszKPuuAa'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
auth.secure=True
api=tweepy.API(auth)

##print(str(api.get_user(screen_name='@kewalkishang'))) testing if connection is set

for tweet in tweepy.Cursor(api.search,q='#MIvGL',lang='en').items(10):
    try:
        print("Found tweet by : @"+ tweet.user.screen_name)
        if (tweet.retweeted==False) or (tweet.favorited==False) :
            tweet.retweet()
            tweet.favorite()
            print("retweeted and fav")

        if tweet.user.following  == False:
            tweet.user.follow()
            print("followed the user")

    except tweepy.TweepError as e:
        print(e.reason)
        sleep(10)
        continue
    except StopIteration:
        break
                    
