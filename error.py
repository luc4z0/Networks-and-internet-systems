import numpy as np
# to help with error problem set

# probablity of a frame being in error
def pf_error(bits, p):
    if (p > 1):
        print("Probabilty must be less than one")
        return
    return 1 - np.power(1-p, bits)

def pf_good(bits, p):
    if (p > 1):
        print("Probabilty must be less than one")
        return
    return np.power(1-p, bits)

def pfHops_error(bits, p, hops):
    return 1 - pfHops_good(bits, p, hops)

def pfHops_good(bits, p, hops):
    return np.power(pf_good(bits, p), hops)

def max_bits(minimal_error, p):
    return np.log(1-minimal_error)/np.log(1-p)

def max_bits_hops(minimal_error, BER, hops):
    return max_bits(minimal_error, BER)/hops

def max_BER_hops(bits, F_error, hops):
    return 1-np.power(F_error, 1/(hops*bits))
