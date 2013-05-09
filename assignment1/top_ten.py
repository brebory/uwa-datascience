import sys
import json
import math
import re

def hw(sent_file, tweet_file):
    sentiments, tweets = process_files(sent_file, tweet_file)
    hashtags = process_tags(tweets).items()
    hashtags.sort(key=extract_key, reverse=True)
    for i in range(10):
        print "%s %f".encode("utf-8") % (hashtags[i][0], float(hashtags[i][1]))

def extract_key(coll):
    return coll[1]


def process_files(sent_file, tweet_file):
    tweets = []
    sentiments = {}
    for line in sent_file:
        term, score = line.split("\t")
        sentiments[term] = float(score)
    for line in tweet_file:
        tweets.append(line)
    return [sentiments, tweets]

def process_tags(tweets):
    result = {}
    for tweet in tweets:
        hashtags = process_tweet_hashtags(tweet)
        if hashtags:
            for tag in hashtags:
                text = tag["text"]
                if text in result:
                    result[text] += 1
                else:
                    result[text] = 1
    return result

def process_tweet_hashtags(tweet):
    try:
        return json.loads(tweet)["entities"]["hashtags"]
    except KeyError:
        return None

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()