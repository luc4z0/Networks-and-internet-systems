#!/usr/bin/env python3
# Use: ./subnet.py <ip/cidr>
# Alt: ./subnet.py <ip> <mask>

import sys

def subnet(addr, mask):
    #addr = [0, 0, 0, 0]
    #mask = [0, 0, 0, 0]
    cidr = 0
            
    netw = [addr[i] & mask[i] for i in range(4)]
    bcas = [(addr[i] & mask[i]) | (255^mask[i]) for i in range(4)]
    
    print("Address: {0}".format('.'.join(map(str, addr))))
    print("Mask: {0}".format('.'.join(map(str, mask))))
    print("Cidr: {0}".format(cidr))
    print("Network: {0}".format('.'.join(map(str, netw))))
    print("Broadcast: {0}".format('.'.join(map(str, bcas))))

def print_bin(addr):
    print(bin(addr[0]),bin(addr[1]),bin(addr[2]),bin(addr[3]))
    return