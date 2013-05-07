import sys
import json
import re

def hw(sent_file, tweet_file):
    scores, tweets = process_files(sent_file, tweet_file)
    scored_words = tweet_sentiments(scores, tweets)
    for word in scored_words:
        print("%f" % scored_words[word])

def tweet_sentiments(scores, tweets):
    result = {}
    for tweet in tweets:
        try:
            text = json.loads(tweet)["text"]
        except KeyError:
            continue
        else:
            result[tweet] = 0
            words = text.split()
            for word in words:
                if re.search(r'[^a-zA-Z]', word):
                    continue
                try:
                    result[tweet] += float(scores[word.lower()])
                except KeyError:
                     continue
    return result
                    


def process_files(sent_file, tweet_file):
    sentiments = {}
    tweets = []
    for line in sent_file:
        term, value = line.split("\t")
        sentiments[term] = float(value)
    for line in tweet_file:
        tweets.append(line)
    return [sentiments, tweets]


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()