import sys
import json
import math
import re

def hw(sent_file, tweet_file):
    sentiments, tweets = load_tweets(sent_file, tweet_file)
    for tweet in tweets:
        try:
            text = json.loads(tweet)["text"]
        except KeyError:
            continue 
        else:
            tweet_sentiments = construct_initial_sentiments(text.split(), sentiments)
            avg_sent = round_average(average_sentiment(tweet_sentiments))
            result = reassign_words(tweet_sentiments, avg_sent)
            print_result(result)

def load_tweets(sent_file, tweet_file):
    tweets = []
    sentiments = {}
    for line in sent_file:
        term, score = line.split("\t")
        sentiments[term] = float(score)
    for line in tweet_file:
        tweets.append(line)
    return [sentiments, tweets]

def construct_initial_sentiments(tweet_text, sentiments):
    tweet_sentiments = {}
    for word in tweet_text:
        if re.search(r'[^a-zA-Z]', word):
            continue
        try:
            tweet_sentiments[word] = float(sentiments[word.lower()])
        except KeyError:
            tweet_sentiments[word] = 0.0
    return tweet_sentiments

def average_sentiment(words_sentiment):
    total_score = 0.0
    number_terms = 0.0
    for word in words_sentiment:
        if(words_sentiment[word] != 0.0):
            total_score += words_sentiment[word]
            number_terms += 1.0
    try:
        return total_score / number_terms
    except ZeroDivisionError:
        return 0.0

def round_average(value):
    if(value > 0.0):
        return math.ceil(value)
    else:
        return math.floor(value)

def reassign_words(wordlist, value):
    for word in wordlist:
        if(wordlist[word] == 0.0):
            wordlist[word] = value
    return wordlist

def print_result(result):
    for word in result:
        print("%s %f" % (word, result[word]))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()