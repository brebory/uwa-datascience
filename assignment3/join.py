import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	# key: id
	# value: rest of records for item
	identifier = record[1]
	mr.emit_intermediate(identifier, record)

def reducer(key, list_of_values):
    # key: id
    # value: records for id. value[0] labels val as either order or line_item
	orders = []
	line_items = []	
	for val in list_of_values:
		identifier = val[0]
		if identifier == u'order':
			orders.append(val)
		else:
			line_items.append(val)
	for order in orders:
		for line_item in line_items:
			mr.emit(order + line_item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
