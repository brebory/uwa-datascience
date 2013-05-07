import sys
import json
import re

def hw(filename):
    tweetfile = open(filename, "r")
    tags = {}
    for line in tweetfile:
        try:
            hashtags = json.loads(line)["entities"]["hashtags"]
        except KeyError:
            print "Didn't have a entities or hashtags entry"
            continue
        else:
            for tag in hashtags:
                try:
                    tags[tag[u'text']] += 1.0
                except KeyError:
                    tags[tag[u'text']] = 1.0
    # Need to implement lambda in sorted(list, cmp <= lambda) here, must research
    for tag in tags:
        print("%s %f" % (tag, tags[tag]))

def lines(fp):
    print str(len(fp.readlines()))

def main():
    hw(sys.argv[1])

if __name__ == '__main__':
    main()