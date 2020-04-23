def get_regions_names(filename):
    ret = {}
    with open(filename, 'r') as fd:
        for index, line in enumerate(fd):
            # ignore header
            if index == 0:
                continue
            name, region = line.strip().split(',')
            ret.update({region:name})
            
    return ret
