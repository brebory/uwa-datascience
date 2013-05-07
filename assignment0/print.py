import urllib
import json

results = []
for i in range(1, 10):
    results.append(urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=%d" % i));

for result in results:
    print json.load(result), "\n"
