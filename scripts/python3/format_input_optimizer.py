import json


class Details:
    def __init__(self, **kwargs):
        try:
            self.type = 'linux'
            self.size = "m5.xlarge"
            self.price= kwargs['price']
            self.storage_cost = kwargs['storage_cost']
        except Exception as e:
            print(e)

class DataCenter:
    def __init__(self, **kwargs):
        try:
            self.id = kwargs['id']
            self.latencies = kwargs['latencies']
            self.network_cost = kwargs['network_cost']
            self.provider = "AWS"
            self.name = kwargs['name']
            self.code = kwargs['code']
            __details = Details(price=kwargs["price"],
                                storage_cost=kwargs['storage_cost'])
            self.details = __details.__dict__
        except Exception as e:
            print(e)


def toDict(filename):
    _dict = {}
    with open(filename) as fd:
        for i, line in enumerate(fd):
            if i == 0:
                continue
            else:
                _region, _price = line.strip().split(',')
                _dict.update({_region:float(_price)})
    return _dict 

def toDict_str(filename):
    _dict = {}
    with open(filename) as fd:
        for i, line in enumerate(fd):
            if i == 0:
                continue
            else:
                _region, _name = line.strip().split(',')
                _dict.update({_region:_name})
    return _dict 

if __name__ == "__main__":
    
    datacenters = []

    l = {}
    b_price = {}
    s_price = {}
    v_price = {}


    # parse latencies   
    with open("latencies.csv") as fd:
        for i, line in enumerate(fd):
            if i == 0:
                continue
            else:
                _region = line.strip().split(',')[0]
                _latencies = line.strip().split(',')[1:]
                _latencies = [int(i) for i in _latencies]
                l.update({_region:_latencies})

    # parse storage, bandwidth and VM prices
    s_price = toDict('EBSGP2_pricing.csv')
    b_price = toDict('bandwidth_price.csv')
    v_price = toDict('c5xlarge_price.csv')
    codes   = toDict_str('all_regions')
    
    for i, key in enumerate(l.keys()):
        _dc = DataCenter(id=i,
                         latencies=l[key],
                         network_cost = b_price[key],
                         name = key,
                         code = codes[key],
                         price= v_price[key],
                         storage_cost = s_price[key])
        datacenters.append(_dc.__dict__)


    datacenters = {"datacenter":datacenters}
    
    json.dump(datacenters, open("18dc.json", "w"), indent=4) 
    











            
             
