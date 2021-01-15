import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

## semi-empirical formula

def binding(A, Z):
    # coefficients
    AV = 15.56
    AS = 17.23
    AC = 0.697
    AA = 23.285
    AP = 12.0
    
    odd = A%2

    if odd:
        APCOEF = -AP/sqrt(A)
    else:
        APCOEF = AP/sqrt(A)
        
    
    B = AV*A - AS*(A**(2/3))
        - AC*Z/(A**(1/3)) 
        - AA*((A -2*Z)**2)/A
        + APCOEFF
    
    return(B)

def semiEmpirical(B, A, Z):
    pass