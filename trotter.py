import matplotlib.pyplot as plt
import numpy as np
from cmath import sqrt, exp, cos, sin, pi
import operacje as q

def Hamiltonian(L:int, J:float, h:float, t:float, n:int, alfa:float)->list:
    # H=-J*Σ(Zi,Zi+1)-h*Σ(sinαZi+cosαXi)
    Z=q.Z
    for i in range(L-1):
        Z=np.kron(Z,q.Z)
    Ha=np.array([[Z[i][j] for j in range(len(Z))] for i in range(len(Z))], dtype=complex)

    for i in range(len(Ha)):
        for j in range(len(Ha)):
            if i==j:
                Ha[i][j]=exp(Ha[i][j]*1.j*J*t/n)
    H=[Ha]

    beta=h*cos(alfa)*t/n
    gamma=h*sin(alfa)*t/n
    Rx=np.array([[cos(beta),1.j*sin(beta)],
                [1.j*sin(beta),cos(beta)]], dtype=complex)
    Rz=np.array([[exp(1.j*gamma),0],
                [0,exp(-1.j*gamma)]], dtype=complex)
    for i in range(L):
        k=L-1
        el1=Rx
        el2=Rz
        while k>i:
            el1=np.kron(q.I,el1)
            el2=np.kron(q.I,el2)
            k-=1
        k-=1
        while k>-1:
            el1=np.kron(el1,q.I)
            el2=np.kron(el2,q.I)
            k-=1
        H.append(el1)
        H.append(el2)
    return H

def Trotter(H:np.array, n:int)->np.array:
    U = np.eye(2**L, dtype=complex)
    Ut = np.eye(2**L, dtype=complex)
    for i in range(len(H)):
        U=np.dot(H[i],U)
    for i in range(n):
        Ut=np.dot(U,Ut)
    return Ut
    # for i in range(len(H)):
    #     U = np.dot(H[i], U)
    # for i in range(n):
    #     U = np.dot(U, U)
    # return U
    # U=np.array([[1,0],
    #             [0,1]])
    # Ut=np.array([[1,0],
    #             [0,1]])
    # for i in range(L-1):
    #     U=np.kron(U,q.I)
    #     Ut=np.kron(Ut,q.I)

if __name__=='__main__':
    L=2
    J=0.2
    h=1
    alfa=pi/4
    psi0=np.array([0,0,1,0], dtype=complex) #|10>
    T=[]
    energie=[]
    n=1000
    for eps in range(1000):
        t=eps/100
        T.append(t)
        H=Hamiltonian(L,J,h,t,n,alfa)
        U=Trotter(H,n)
        psit=np.dot(U,psi0)
        He=np.array([[0 for i in range(len(H[0]))] for j in range(len(H[0]))],dtype=complex)
        for i in range(len(H)-1):
            He+=H[i]+H[i+1]
        energia=np.dot(He,psit)
        energia=np.abs(np.dot(np.transpose(np.conjugate(psit)),energia))
        energie.append(energia)
    T=np.array(T)
    energie=np.array(energie)
    plt.plot(T, energie, '.', label=f'n={n}')
    plt.xlabel('czas')
    plt.ylabel('energia')
    plt.legend()
    plt.show()
    # psit /= np.linalg.norm(psit)
    # print(psit)
    # quit()
    # prob = np.abs(psit)**2
    # prob=[]
    # for i in range(len(psit)):
    #     prob.append(abs(psit[i])**2)
    # print(prob)
