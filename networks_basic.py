import numpy as np

def upload_time(size, upload_speed):
    return size / upload_speed

def sum_of_peaks(flows):
    _sum = 0
    for flow in flows:
        _max = max(flow)
        _sum = _max + _sum
    return _sum

def TCP(MSS, R_Window, threshold, transmitions, timeout=0):
    congestion = MSS
    print("Initialising transmittion. MSS=",MSS,"Recievers Advertised window=",R_Window)
    print("Transmition number",1,"\tCongestion Window=", congestion, "\tthreshold=", threshold)
    for t in range(2,transmitions + 1, 1):
        if (t == timeout):
            threshold = int(congestion/2)
            congestion = MSS
        else:
            if (congestion >= R_Window):
                congestion = R_Window
            else:
                if (congestion >= threshold):
                    if ((congestion + MSS) >= R_Window):
                        congestion = R_Window
                    else:
                        congestion += MSS #linear
                else:
                    if (congestion * 2 >= threshold):
                        congestion = threshold
                    else:
                        congestion = congestion * 2
        print("===================================================================")
        print("Transmition number",t,"\tCongestion Window=", congestion, "\tthreshold=", threshold)

def propagation_delay(meters, velocity):
    return meters / velocity




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


