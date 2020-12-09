from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = 'pYoPARudnBJeg6VOos87eRL1I'
consumer_secret_key = '8fubRmzWeS8Iaor9KHDfgMivDEMsjGKPf64nZre9EnV2IWHnvU'
access_key = 'EMuVRHgtJj0yby1cPFgOavtdSJJQwfkdZOcn4IxjShfyQ'
access_key_secret = 'EMuVRHgtJj0yby1cPFgOavtdSJJQwfkdZOcn4IxjShfyQ'


class MyStreamListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        # if status_code == 420:
        #     return False
        if status == 401:
            print(status)
            return False
        print(status)

    # def on_status(self, status):
    #     print(status.text)


if __name__ == "__main__":
    auth = OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_key, access_key_secret)
    api = API(auth)

    listener = MyStreamListener()
    stream = Stream(api.auth, listener)
    stream.filter(track=['Donald Trump', 'Barack Obama', 'Joe Biden'])

