import sys
import json
import math

def hw():
    affin = open("AFINN-111.txt", "r")
    sentiments, tweets = load_tweets(affin, "output.txt")
    for tweet in tweets:
        try:
            text = json.loads(tweet)["text"]
        except KeyError:
            continue 
        else:
            tweet_sentiment = construct_initial_sentiments(text.split(" "), sentiments)
            avg_sent = round_average(average_sentiment(tweet_sentiment))
            result = reassign_words(tweet_sentiment, avg_sent)
            print_result(result)

def load_tweets(affin, filename):
    result = []
    sentiments = {}
    for line in affin:
        term, score = line.split("\t")
        sentiments[term] = float(score)
        tweetfile = open(filename, "r")
        for line in tweetfile:
            result.append(line)
    return [sentiments, result]

def round_average(value):
    if(value > 0.0):
        return math.ceil(value)
    else:
        return math.floor(value)

def print_result(result):
    for word in result:
        print("%s %f" % (word, result[word]))

def construct_initial_sentiments(wordlist, sentiments):
    sentiment_dict = {}
    for word in wordlist:
        try:
            sentiment_dict[word] = float(sentiments[word.lower()])
        except KeyError:
            sentiment_dict[word] = 0.0
    return sentiment_dict


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

def reassign_words(wordlist, value):
    for word in wordlist:
        if(wordlist[word] == 0.0):
            wordlist[word] = value
    return wordlist

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
