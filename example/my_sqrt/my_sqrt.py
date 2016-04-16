def mySqrt(n):
    C = n
    x0 = C/2.0
    x = x0
    while (x**2-C)**2 > 0.001:
        next_x = x - (x**2-C)/(2*x)
        x = next_x
    return x
