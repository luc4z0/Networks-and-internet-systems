import math

# when we dont care about the number of inputs 
def opt_nm(N, stage):
    # Calculate initial values for m and n
    temp = (stage + 1) / 2
    m = int(math.sqrt(N * temp))
    n = int(math.sqrt(N / temp))

    # Initialize the minimum product and corresponding m and n
    min_product = float('inf')
    min_m = 0
    min_n = 0

    # Iterate through all possible combinations of m and n
    for i in range(m, N + 1):
        for j in range(n, N + 1):
            product = i * j
            if product >= N and product < min_product:
                min_product = product
                min_m = i
                min_n = j

    return [min_m, min_n]

# when we do care about n being exact same as inputs
def find_closest_factors(N, m):
    unrounded_m = m
    m = round(m)
    if N <= 0:
        return None, None  # There are no factors for non-positive numbers.

    # Initialize variables to None.
    closest_factor_up = 0
    closest_factor_down = 0

    # Start counting upwards from m to find the first factor.
    i = m
    while i <= N:
        if N % i == 0:
            closest_factor_up = i
            break
        i += 1

    # Start counting downwards from m to find the first factor.
    i = m
    while i >= 1:
        if N % i == 0:
            closest_factor_down = i
            break
        i -= 1


    # Calculate the absolute differences from m for both factors.
    diff_up = abs(closest_factor_up - unrounded_m) + abs(N / closest_factor_up - N / unrounded_m)
    diff_down = abs(closest_factor_down - unrounded_m) + abs(N / closest_factor_down - N / unrounded_m)

    # Return the closer of the two factors.
    if diff_up < diff_down:
        return closest_factor_up#, diff_up
    else:
        return closest_factor_down#, diff_down
    
