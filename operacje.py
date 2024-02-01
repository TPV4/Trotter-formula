import numpy as np
from math import sqrt, sin, cos, exp, pi
import cmath as c

def diag(M:np.array)->list:
    eig=np.linalg.eig(M) #lista wartości własnych i wektorów własnych
    eigVAL=eig[0]
    eigVEC=eig[1]
    D=np.array([[0 for i in range(len(eigVAL))] for i in range(len(eigVAL))], dtype=complex)
    for i in range(len(eigVAL)):
        D[i][i]=eigVAL[i]
    P=np.array([eigVEC[i] for i in range(len(eigVEC))], dtype=complex)
    P=np.transpose(P)
    Pinv=np.linalg.inv(P)
    Md=[P,D,Pinv]
    return Md

I=np.array([[1,0],
            [0,1]])
X=np.array([[0,1],
            [1,0]])
Y=np.array([[0,-1.j],
            [1.j,0]])
Z=np.array([[1,0],
            [0,-1]])
H=np.array([[sqrt(2)/2,sqrt(2)/2],
            [sqrt(2)/2,-sqrt(2)/2]])