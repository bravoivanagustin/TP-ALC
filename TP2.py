import numpy as np
import random as rd

def metodoPotencia(A,v,n):
    v0 = np.copy(v)
    for i in range(n):
        v0 = A@v0
        v0 = v0/np.linalg.norm(v0)
    return np.sum(A@v0)/np.sum(v0)

def montecarlo(A, n, m):
    prom = 0
    for i in range(n):    
        v = [rd.random() for i in range(len(A))]
        v = np.array(v)
        if (np.linalg.norm(v) == 0):
            v = np.ones(len(A))
        v = v/np.linalg.norm(v)
        prom += metodoPotencia(A,v,m)
    prom /= n
    return prom

A = np.array([[1,2,1],[1,-1,1],[1,5,1]])
v = np.array([0,1,0])

print(montecarlo(A, 250, 100))
print(np.linalg.eigvals(A)[0])
print(metodoPotencia(A,v,1000))