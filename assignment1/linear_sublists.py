def linear_sublists(coll):
    """
    Given a collection, returns a list of the linear sublists
    """
    result = []
    for i in range(len(coll)):
        subcoll1 = coll[i:]
        subcoll2 = coll[:i]
        if subcoll1 not in result and len(subcoll1):
            result.append(coll[i:])
        if subcoll2 not in result and len(subcoll2):
            result.append(coll[:i])
        for j in range(i, len(coll)):
            subcoll3 = coll[i:j]
            if subcoll3 not in result and len(subcoll3):
                result.append(coll[i:j])
    return result

def main():
    print linear_sublists([1, 2, 3, 4])
    print linear_sublists([])
    print linear_sublists([1, 2, 3])

if __name__ == '__main__':
    main()