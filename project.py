import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

## semi-empirical formula

def binding(A, Z):
    # coefficients MeV
    AV = 15.56
    AS = 17.23
    AC = 0.697
    AA = 23.285
    AP = 12.0
    
    Aodd = A%2
    Zodd = Z%2

    if (Aodd + Zodd) == 2:
        APCOEF = -AP/sqrt(A)
    elif (Aodd + Zodd) == 1:
        APCOEF = 0
    else:
        APCOEF = AP/sqrt(A)
        
    
    B = AV*A - AS*(A**(2/3)) - AC*(Z**2)/(A**(1/3)) - AA*((A -2*Z)**2)/A + APCOEF
    
    return(B)

def semiEmpirical(A, Z):
    # constants MeV
    MP = 938.280
    MN = 939.573

    B = binding(A, Z)

    Mass = Z*MP + (A - Z)*MN - B

    return(Mass)

A99 = np.arange(41, 48)
A98 = np.arange(42, 45)

Mass99 =[]
Mass98 =[]
for Z in A99:
    Mass99.append(semiEmpirical(99, Z))
for Z in A98:
    Mass98.append(semiEmpirical(98, Z))

plt.scatter(A99, Mass99, vmin=True)
plt.xlabel('Z')
plt.ylabel('Mass')
plt.title('A=99')
plt.show()
plt.scatter(A98, Mass98)
plt.xlabel('Z')
plt.ylabel('Mass')
plt.title('A=98')
plt.show()

i = 0
Mo = 200
Tc = 100
while True:
    Mo /= 2
    Tc += Mo
    Tc /= 2
    i += 1
    if Tc <= 10 and Mo <= 10:
        print(i)
        break
    else:
        pass