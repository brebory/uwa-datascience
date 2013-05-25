import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	# key: document identifier
	# value: document contents
	key = record[0]
	value = record[1]
	words = value.split()
	emitted = {}
	for w in words:
		if w not in emitted:
			mr.emit_intermediate(w, key)
			emitted[w] = True

def reducer(key, list_of_values):
    # key: word
    # value: list of docids containing word 
    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
