import sys
import json

def hw():
    affin = open("AFINN-111.txt", "r")
    scores = {}
    tweets = []
    index = 0
    for line in affin:
        term, score = line.split("\t")
        scores[term] = int(score)
        tweetfile = open("output.txt", "r")
        for line in tweetfile:
            tweets.append(line) 
    for tweet in tweets:
        index += 1
        tweetscore = 0.0
        try:
            text = json.loads(tweet)["text"]
        except KeyError:
            continue 
        else:
            words = text.split(" ")
            for word in words:
                try:
                    tweetscore += float(scores[word.lower()])
                    
                except KeyError:
                    continue
            print("%f" % tweetscore)


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