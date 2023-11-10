import math
import helper 
N = 2880

def crossbar(N):
    switches = N * N
    print("Crossbar switch, number of inputs N = ", N, " Number of crosspoints = ", switches)
    return switches

def clos(N, stage):
    mn = helper.opt_nm(N, stage) # [m , n]
    if (stage < 3):
        return N * N
    switches = 2 * (mn[0] * mn[1] * (2 * mn[1] - 1)) + (2 * mn[1] - 1) * (clos(mn[0], stage - 2))
    print(" Clos switch (stage ", stage , "). N = ", N, " m = ", mn[0], " n = ", mn[1], " Total number of inputs =", mn[0] * mn[1], " Total number of crosspoints = ", switches)
    return switches

def clos_exactN(N, stage):
    mn = []
    mn.append(helper.find_closest_factors(N, math.sqrt(N * ((stage + 1) / 2)))) # [m , n]
    mn.append(round(N / mn[0])) 
    if (stage < 3):
        return N * N
    switches = 2 * (mn[0] * mn[1] * (2 * mn[1] - 1)) + (2 * mn[1] - 1) * (clos_exactN(mn[0], stage - 2))
    print("Clos switch (Exact) (stage ", stage , "). N = ", N, " m = ", mn[0], " n = ", mn[1], " Total number of inputs =", mn[0] * mn[1], " Total number of crosspoints = ", switches)
    return switches

def clos_choose(N, stage):
    if (stage < 3):
        return N * N
    print("Stage ", stage)
    mn = []
    mn.append(int(input("m = ")))
    mn.append(int(input("n = ")))
    print("Clos switch (Choose) (stage ", stage , "). N = ", N, " m = ", mn[0], " n = ", mn[1], " Total number of inputs =", mn[0] * mn[1])
    switches = 2 * (mn[0] * mn[1] * (2 * mn[1] - 1)) + (2 * mn[1] - 1) * (clos_choose(mn[0], stage - 2))
    return switches

def Moore(N):
    n = round(N / 2)
    switches = 6 * n * n + 6 * n
    print("Moore Switch. N = ", N, " Total number of crosspoints = ", switches)
    return switches

def Slepian(N, stage):
    rn = helper.opt_nm(N, stage) # [ r , n]
    if ( stage < 3):
        return N * N
    switches = 2 * (rn[0] * rn[1] * rn[1]) + rn [1] * (Slepian(rn[0], stage - 2))
    print("Slepian switch (stage ", stage , "). N = ", N, " r = ", rn[0], " n = ", rn[1], " Total number of crosspoints = ", switches)
    return switches

def Slepian_exactN(N, stage):
    rn = []
    rn.append(helper.find_closest_factors(N, math.sqrt(N))) # [m , n]
    rn.append(round(N / rn[0]))
    if ( stage < 3):
        return N * N
    switches = 2 * (rn[0] * rn[1] * rn[1]) + rn [1] * (Slepian_exactN(rn[0], stage - 2))
    print("Slepian switch (Exact)(stage ", stage , "). N = ", N, " r = ", rn[0], " n = ", rn[1], " Total number of crosspoints = ", switches)
    return switches

def Slepian_choose(N, stage):
    if ( stage < 3):
        return N * N
    rn = []
    rn.append(int(input("r = ")))
    rn.append(int(input("n = ")))
    print("Slepian switch (choose)(stage ", stage , "). N = ", N, " r = ", rn[0], " n = ", rn[1])
    switches = 2 * (rn[0] * rn[1] * rn[1]) + rn [1] * (Slepian_choose(rn[0], stage - 2))
    return switches

def Slepian_Rev(size_of_inner, N):
    k = math.ceil(math.log(N, size_of_inner) - 1)
    print(k)
    stages = 2 * k + 1
    switches = size_of_inner * size_of_inner**(k+1) * stages
    print("Slepian using only ",size_of_inner,"x",size_of_inner," crossbars. N = ", 3**(k+1), " Number of stages = ", stages, " Crosspoints = ", switches)
    return switches

def lower_bound(N):
    return math.ceil(N * math.log(N, 2))


clos(6020, 3)
