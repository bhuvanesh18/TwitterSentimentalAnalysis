import re
import tweepy
from textblob import TextBlob
from django.shortcuts import render
from django.http import HttpResponse

class TwitterClient(object):
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity >= 0:
            return 'Positive'
        else:
            return 'Negative'

    def get_tweets(self, query):
        tweets = []
        try:
            parsed_tweet = {}
            parsed_tweet['text'] = query
            parsed_tweet['sentiment'] = self.get_tweet_sentiment(query)
            tweets.append(parsed_tweet)
            return tweets
        except tweepy.TweepError as e:
            print("Error : " + str(e))

def main(request):
    usertweet = request.POST['utweet']
    api = TwitterClient()
    tweets = api.get_tweets(query=usertweet)
    passon_value = [x for x in tweets[0].values()]
    # return HttpResponse('<center><h3>{0}<h3><h1>{1}</h1></center>'.format(tweets[0]['text'], tweets[0]['sentiment']))
    return render(request, 'TweetAnalysisApp/result.html',context = {'tweet': passon_value[0], 'sentiment':passon_value[1]})