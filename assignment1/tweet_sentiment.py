import sys
import json
import re

def hw(sent_file, tweet_file):
    sentiments, tweets = process_files(sent_file, tweet_file)
    scored_tweets = tweet_sentiments(sentiments, tweets)
    for tweet in tweets:
        text = process_tweet(tweet)
        if text:
            print("%f" % float(scored_tweets[text]))

def tweet_sentiments(sentiments, tweets):
    """
    Creates a dictionary of tweet: sentiment pairs where
    sentiment is the sum of sentiments of all terms in tweet
    """
    result = {}
    for tweet in tweets:
        text = process_tweet(tweet)
        if text:
            phrases = text.split()
            tweet_sentiment = 0.0
            for phrase in phrases:
                tweet_sentiment += word_sentiment(sentiments, phrase)
            result[text] = tweet_sentiment
    return result

def extract_words_and_phrases(wordlist):
    """
    Given a list built from a sentence in order of occurance, builds
    a list of all possible phrases that could be extracted from that sentence
    including just individual words.
    Returns the list of words and phrases
    """
    phrases_list = linear_sublists(wordlist)
    result = []
    for word_list in phrases_list:
        result.append(stringify(word_list))
    return result

def stringify(coll):
    """
    Returns all members of coll concatenated into one string.
    """
    return " ".join(coll)

    
def linear_sublists(coll):
    """
    Given a collection, returns a list of the linear sublists
    """
    result = []
    l = len(coll)
    for i in range(l):
        for j in range(i + 1, l):
            result.append(coll[i:j])
    return result

def process_tweet(tweet):
    try:
        return json.loads(tweet)["text"]
    except KeyError:
        return None

def word_sentiment(sentiments, word):
    try:
        return float(sentiments[word.lower()])
    except KeyError:
        return 0.0

def process_files(sent_file, tweet_file):
    sentiments = {}
    tweets = []
    for line in sent_file:
        term, value = line.split("\t")
        sentiments[term] = float(value)
    for line in tweet_file:
        tweets.append(line)
    return (sentiments, tweets)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()