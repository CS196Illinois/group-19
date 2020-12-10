from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Cursor
import pandas as pd

consumer_key = 'MM6r2egdzoGeNA089JwUVntla'
consumer_secret_key = 'kuy3aYgua2t8EN670NRRjMeukwCpbZXLsKm5HCgSTeJTIQCF6L'
access_key = '1084201829574025216-iBAR68hvwTZ5TDIIBep2FtZbghdvJ0'
access_key_secret = 'U2ZUlCxEr8aWGw1GPvCTNarsTqhOrkLRiP3Oul4UTjFip'


class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler( consumer_key, consumer_secret_key )
        auth.set_access_token( access_key, access_key_secret )
        return auth


class TwitterClient():
    """
    Class that provides different access points for twitter.
    """

    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


class TwitterStreamer():
    """
    Class for processing and streaming live tweets
    """

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()


    def stream_tweets(self, fetched_tweets_filename, hashtag_list):
        # This handles twitter authentication and connection to the twitter stream API
        auth = self.twitter_authenticator.authenticate_twitter_app()

        listener = TwitterListener( fetched_tweets_filename )
        stream = Stream( auth, listener )
        stream.filter( track=hashtag_list, is_async=True )


class TwitterListener( StreamListener ):
    """
    This is a basic listener class that prints received tweets to StdOut
    """

    def __init__(self, fetched_tweets_filename, i=0):
        self.fetched_tweets_filename = fetched_tweets_filename
        self.i = i

    def on_data(self, data):
        while (self.i < 10000):
            try:
                with open(self.fetched_tweets_filename, 'a') as tf:
                    tf.write(data)
                return True
            except BaseException as e:
                print("Error_on_data: %s" % str(e))
            finally:
                self.i += 1
                print(self.i)
                return True
        return False

    def on_error(self, status):
        if status == 420:
            print(status)
            return False
        if status == 401:
            print(status)
            return False


class TweetAnalyzer():
    """
    Processes twitter information into dataframe
    """

    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        return df


class GoTime():
    """
    Final execution for Moody Models project.
    """

    def clear_files(self):

        # Clear JSON file for fresh scrape
        file = open("tweets.json", "r+")
        file.truncate(0)
        file.close()

        # # Clear TXT file for fresh scrape
        # file = open("tweetsToText.txt", "r+")
        # file.truncate(0)
        # file.close()

    def stream_command(self):

        hashtag_list = ['Home', 'World', 'US', 'Politics', 'Economy',
                        'Business', 'Tech', 'Markets', 'Opinion', 'Life', 'Art']
        filename = "tweets.json"

        streamer = TwitterStreamer()
        streamer.stream_tweets(filename, hashtag_list)