import numpy as np

def upload_time(size, upload_speed):
    return size / upload_speed

def sum_of_peaks(flows):
    _sum = 0
    for flow in flows:
        _max = max(flow)
        _sum = _max + _sum
    return _sum




Irish_times = {'size': 2000, 'speed': 4e6}
Independent = {'size': 8e6, 'speed': 3e6}
RTE = {'size': 6e6, 'speed': 5e6}

companies = [Irish_times, Independent, RTE]
for company in companies:
    upload_time(company['size'], company['speed'])

flows = {'F1': [1, 8, 3, 15, 2, 1, 1, 34, 3, 4], 
         'F2': [6, 2, 5, 5, 7, 40, 21, 3, 34, 5],
         'F3': [45, 34, 15, 5, 7, 9, 21, 5, 3, 34]}


max_peaks = 0
for key in flows:
    _max = max(flows[key])
    _sum = sum(flows[key])
    print(key, "Max = ", _max ,": sum = ", _sum)
    max_peaks = max_peaks + _max 

aggregate = [flows['F1'][i] + flows['F2'][i] + flows['F3'][i] for i in range(len(flows['F1']))]


