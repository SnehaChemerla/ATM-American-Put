# -*- coding: utf-8 -*-
import numpy as np
import math as m
import random


def AmPutCRR(S0,K,r,T,sigma,N):
    deltaT=T/N
    u=m.exp(sigma*m.sqrt(deltaT))
    d=1/u
    a=m.exp(r*deltaT)
    p=(a-d)/(u-d) 
    S = []
    
    P = np.zeros((N+1,N+1))
    I = []
    Time = np.zeros((N+1,N+1))
    Time[:,N] = T*np.ones(N+1);
    for i in range(0,N+1):
        Val=[]
        Ind=[]
        for j in range(0,i+1):
            V = S0*((u**(i-j))*(d**(j)))
            Ind.append(max(K-V,0))
            Val.append(V)
        S.append(Val)
        I.append(Ind)
    Q=[None]*(N+1)
    Q[N] = I[N]
    for i in range(N-1,-1,-1):
        X = []
        for j in range(0,i+1):
            E = p*Q[i+1][j]/a+(1-p)*Q[i+1][j+1]/a;
            X.append(max(E,I[i][j]))
        Q[i] = X
    price = Q[0]
    
        

def Greeks(S0,K,r,T,sigma,N):
    Delta1 = AmPutCRR(100,100,0.05,1,0.3,50) -AmPutCRR(101,100,0.05,1,0.3,50)
    Delta2 = AmPutCRR(101,100,0.05,1,0.3,50) -AmPutCRR(102,100,0.05,1,0.3,50)
    Gamma = Delta1-Delta2
    Theta = (AmPutCRR(100,100,0.05,1,0.3,50) -AmPutCRR(100,100,0.05,366/365,0.3,50))*365
    return Delta1,Gamma,Theta
Optionprice = AmPutCRR(100,100,0.05,1,0.3,50)
delta1,gamma,theta = Greeks(100,100,0.05,1,0.3,50)
print(Optionprice,delta1,gamma,theta)

