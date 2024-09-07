import numpy as np
from scipy.linalg import solve_triangular

def calcularLU(A):

    L = 1*np.eye(len(A), k = 0) #Ya hago la identidad de una
    L = L.astype(float)
    U = np.copy(A) #Copio A, la voy a ir triangulando, preguntar si lo podemos tomar valido esto?
    U = U.astype(float) #paso todo tiplo float, evitar lio
    P = np.eye(len(A), k = 0)
    P = P.astype(float)

    for i in range(0, min([len(U), len(U[0])])): #por si no llega a ser cuadrada uso min, recorrer filas de U y columnas de L
        p = U[i][i]
        for j in range(i+1, len(U)): #recorrer columnas de U y filas de L
            if p != 0:
                c = U[j][i]/p
                U[j] = U[j] - (U[i]*(c)) #Triangulo U
                L[:,i] = L[:,i] + (L[:,j]*(c)) #Modifico las columnas de L, por el factor de traingulacion de U
            elif U[j][i] != 0:
                B = np.copy(U[i]) #Por si llega a haber cero, esto va??? Porque no devolveria A = L.U, preguntar.
                U[i] = U[j]
                U[j] = B
                C = np.copy(P[i]) #P es mi pivote, preguntar como vamos a hacer esto nosotros
                P[i] = P[j] 
                P[j] = C
                if i > 0:
                    D = np.copy(L[i,0:i])
                    L[i,0:i] = L[j,0:i]  #Voy cambiando las partes de L en funcion de las filas intercambiadas
                    L[j,0:i] = D         #Solo tengo que cambiar abajo y antes de la diagonal
                p = U[i][i] 
            else:
                continue #Nada :P
    return L, U, P


def inversaLU(L, U, P):

    L = L.astype(float)
    U = U.astype(float)
    P = P.astype(float)
    P_1 = np.transpose(P)

    I = np.eye(len(L), k = 0) #Identidad

    L_1 = solve_triangular(L, I, lower = True) #Resolver L.x = I, entonces x = L^-1
    U_1 = U_1 = solve_triangular(U, I, lower = False)  #Analogo para U

    Inv = U_1 @ L_1 @ P_1
    return Inv

A = np.array([[0.3,0.0,0.1],[0.05,1.0,0.2],[0.1,0.15,0.1]])
I = np.eye(len(A), k = 0)
B = I-A
d = np.array([100,100,300])
L, U, P = calcularLU(B)
B_1 = inversaLU(L, U, P)
p = B_1 @ d
print(p) 