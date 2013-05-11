import sys
import json
import math
import re

def hw(sent_file, tweet_file):
    sentiments, tweets = process_files(sent_file, tweet_file)
    scored_tweets = tweet_sentiments(sentiments, tweets)
    estimated_sentiments = compute_estimated_sentiments(scored_tweets)
    for key, val in estimated_sentiments.items():
        print "%s %f".encode('utf-8') % (key.encode('utf-8'), float(val["avg"]))

def process_files(sent_file, tweet_file):
    tweets = []
    sentiments = {}
    for line in sent_file:
        term, score = line.split("\t")
        sentiments[term] = float(score)
    for line in tweet_file:
        tweets.append(line)
    return [sentiments, tweets]

def tweet_sentiments(sentiments, tweets):
    result = {}
    for tweet in tweets:
        text = process_tweet(tweet)
        if text:
            #phrases = extract_words_and_phrases(text.split())
            phrases = text.split()
            tweet_sentiment = 0.0
            for phrase in phrases:
                tweet_sentiment += word_sentiment(sentiments, phrase)
            result[text] = tweet_sentiment
    return result

def compute_estimated_sentiments(scored_tweets):
    result = {}
    for tweet in scored_tweets.keys():
        score = scored_tweets[tweet]
        #for phrase in extract_words_and_phrases(tweet.split()):
        for phrase in tweet.split():
            if phrase not in result:
                result[phrase] = {"avg": scored_tweets[tweet], "count": 1.0}
            else:
                avg = result[phrase]["avg"]
                count = result[phrase]["count"]
                result[phrase] = {"avg": (avg * count + score) / (count + 1.0), "count": count + 1.0}
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

def empty(coll):
    return bool(len(coll))

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

def print_result(result):
    for word in result:
        print("%s %f".encode("utf-8") % (word, result[word]))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()