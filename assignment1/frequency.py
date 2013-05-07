import sys
import json
import re

def hw(filename):
    tweetfile = open(filename, "r")
    tweets = {}
    num_terms = 0.0
    for line in tweetfile:
        try:
            text = json.loads(line)["text"]
        except KeyError:
            continue
        else:
            num_terms += float(len(text.split()))
            for term in text.split():
                if re.search(r'[^a-zA-Z]', term):
                    continue
                if term in tweets:
                    tweets[term] += 1.0
                else:
                    tweets[term] = 1.0
    for term in tweets:
        print("%s %f" % (term, tweets[term] / num_terms))


def lines(fp):
    print str(len(fp.readlines()))

def main():
    hw(sys.argv[1])

if __name__ == '__main__':
    main()