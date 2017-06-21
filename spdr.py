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

def calc_for(sym, data_file_path):
    a = parse_file(data_file_path)
    back_12 = a[12:]
    back_6 = a[6:]
    back_3 = a[3:]
    back_1 = a[1:]
    return {12: list(map(calc, back_12, a)),
            6: list(map(calc, back_6, a)),
            3: list(map(calc, back_3, a)),
            1: list(map(calc, back_1, a))}

def summarize(map_list):
    result = []
    for i in range(len(map_list.get(12))):
        (dates12, rs12) = map_list.get(12)[i]
        (dates6, rs6) = map_list.get(6)[12-6+i]
        (dates3, rs3) = map_list.get(3)[12-3+i]
        (dates1, rs1) = map_list.get(1)[12-1+i]
##        print("dates12:", dates12, "rs12=", rs12)
##        print("dates6:", dates6, "rs6=", rs6)
##        print("dates3:", dates3, "rs3=", rs3)
##        print("dates1:", dates1, "rs1=", rs1)
        result.append((dates12[0], rs12+rs6+rs3+rs1))
    return result

spdrs = ['XLB', 'XLE', 'XLF', 'XLI', 'XLK', 'XLP', 'XLRE', 'XLV', 'XLY', 'XLU']

def process(symbols):
    results = {}
    for s in symbols:
        path = '/Users/swav/dev/projects/python/spdr-etf/data/{}.csv'.format(s)
        print('loading: {}'.format(path))
        s_calc = calc_for(s, path)
        results[s] = summarize(s_calc)

    return results


if __name__ == '__main__':
    r = process(spdrs)
##    xlp = calc_for('XLP', '/Users/swav/dev/projects/python/spdr-etf/data/XLP.csv')
##    xlp_summary = summarize(xlp)
##
##    xly = calc_for('XLY', '/Users/swav/dev/projects/python/spdr-etf/data/XLY.csv')
##    xly_summary = summarize(xly)
##
##    xle = calc_for('XLE', '/Users/swav/dev/projects/python/spdr-etf/data/XLY.csv')
##    xle_summary = summarize(xle)

        
        
    
##>>> xlp.get(12)[0]
##(((2000, 1, 1), (1999, 1, 1)), -0.14079250975682303)
##>>> xlp.get(6)[0]
##(((1999, 7, 1), (1999, 1, 1)), -0.0812766031974639)
##>>> xlp.get(3)[0]
##(((1999, 4, 1), (1999, 1, 1)), -0.04836415693621042)
##>>> xlp.get(1)[0]
##(((1999, 2, 1), (1999, 1, 1)), -0.010607522399974314)
