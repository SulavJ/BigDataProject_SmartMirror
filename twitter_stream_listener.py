from pprint import pprint

# consumer key, consumer secret, access token, access secret.
ckey = '3pj4p6mK825Cmxccbtv3fScyw'
csecret = '5j4xGmN2vqj1L4F7aiOBdr2ScfJ38IpUJm6uwb8sHD1xZpq8H7'
atoken = '1098954255409520640-KCxSJROQrgOFX1FhlniZ5yczZsA4D3'
asecret = 'jelXpew819a7NxmxnGpyFIJtcSmQQKXhsAW5VoVtzJbXF'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from smartmirror import TwitterTweetListener
# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self, parent):
        self.parent = parent
        pass

    def stream_tweets(self, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = TwitterTweetListener(self.parent)
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        self.stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        return self.stream.filter(track=hash_tag_list, is_async=True)

    def disconnect(self):
        self.stream.disconnect()


if __name__ == '__main__':
    hashtag_list = ['CWC19']
    obj = TwitterStreamer()
    print(obj.stream_tweets(hashtag_list))