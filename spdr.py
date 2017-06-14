def parse_file(file_path):
    f = open(file_path, 'r')
    res = []
    f.readline() #discard the header
    for line in f:
        attrs = line.split(',')
        date = attrs[0].split('-')
        res.append(((int(date[0]), int(date[1]), int(date[2])), float(attrs[-2])))

    f.close()
    return res    

def calc(shorter_list_tuple, longer_list_tuple):
	ds, ps = shorter_list_tuple
	dl, pl = longer_list_tuple
	return ((ds, dl), (ps-pl)/ps)    

def main():
    a = parse_file('/Users/swav/dev/projects/python/spdr-etf/data/XLP.csv')
    b = a[12:]
    return list(map(calc, b, a))

#>>> c = main()
#>>> c[0]
#(((2000, 1, 1), (1999, 1, 1)), -0.14079250975682303)
