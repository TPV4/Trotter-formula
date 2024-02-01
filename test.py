import operacje as q
import numpy as np
from cmath import exp, cos, sin, pi
import sympy as sy
# from trotter import diag
# alfa=pi/4
# tn=0.001
# beta=cos(alfa)*tn
# gamma=sin(alfa)*tn
# Rx=np.array([[cos(beta),1.j*sin(beta)],
#             [1.j*sin(beta),cos(beta)]], dtype=complex)
# Rz=np.array([[exp(1.j*gamma),0],
#             [0,exp(-1.j*gamma)]], dtype=complex)
# print(np.kron(Rx,q.I))
# print(np.dot(q.X,q.I))
# print(q.X*q.I)
psi=np.array([[0,0,1,0],
             [1,0,0,1.j]], dtype=complex)
print(np.conjugate(np.transpose(psi)))
# U=np.kron(q.I,q.X)
# psi=np.dot(U,psi)
# print(psi)