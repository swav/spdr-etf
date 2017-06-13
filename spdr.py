def parse_file(file_path):
    f = open(file_path, 'r')
    res = []
    f.readline() #discard the header
    for line in f:
        attrs = line.split(',')
        date = attrs[0].split('-')
        res.append(((int(date[0]), int(date[1]), int(date[2])), attrs[-1]))

    f.close()
    return res    
