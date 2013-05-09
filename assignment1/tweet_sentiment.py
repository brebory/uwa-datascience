import sys
import json
import re

def hw(sent_file, tweet_file):
    sentiments, tweets = process_files(sent_file, tweet_file)
    scored_tweets = tweet_sentiments(sentiments, tweets)
    for tweet in scored_tweets:
        print("%f".encode("utf-8") % float(scored_tweets[tweet]))

def tweet_sentiments(sentiments, tweets):
    result = {}
    for tweet in tweets:
        text = process_tweet(tweet)
        if text:
            phrases = text.split()
            tweet_sentiment = 0.0
            for phrase in phrases:
                tweet_sentiment += word_sentiment(sentiments, phrase)
            result[tweet] = tweet_sentiment
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
    return "".join(coll)

    
def linear_sublists(coll):
    """
    Given a collection, returns a list of the linear sublists
    """
    result = []
    for i in range(len(coll)):
        subcoll1 = coll[i:]
        subcoll2 = coll[:i]
        if subcoll1 not in result and len(subcoll1):
            result.append(coll[i:])
        if subcoll2 not in result and len(subcoll2):
            result.append(coll[:i])
        for j in range(i, len(coll)):
            subcoll3 = coll[i:j]
            if subcoll3 not in result and len(subcoll3):
                result.append(coll[i:j])
    return result

def process_tweet(tweet):
    try:
        return json.loads(tweet)["text"]
    except KeyError:
        return None

def word_sentiment(sentiments, word):
    try:
        return float(sentiments[word])
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