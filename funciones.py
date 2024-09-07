import numpy as np
from scipy.linalg import solve_triangular

def calcularLU(A):

    L = 1*np.eye(len(A), k = 0) #Ya hago la identidad de una
    L = L.astype(float)
    U = np.copy(A) #Copio A, la voy a ir triangulando, preguntar si lo podemos tomar valido esto?
    U = U.astype(float) #paso todo tiplo float, evitar lio

    for i in range(0, min([len(U), len(U[0])])): #por si no llega a ser cuadrada uso min, recorrer filas de U y columnas de L
        p = U[i][i]
        for j in range(i+1, len(U)): #recorrer columnas de U y filas de L
            if p != 0:
                c = U[j][i]/p
                U[j] = U[j] - (U[i]*(c)) #Triangulo U
                L[:,i] = L[:,i] + (L[:,j]*(c)) #Modifico las columnas de L, por el factor de traingulacion de U
            #elif U[j][i] != 0:
            #    B = np.copy(U[i]) #Por si llega a haber cero, esto va??? Porque no devolveria A = L.U, preguntar.
            #    U[i] = U[j]
            #    U[j] = B
            #    p = U[i][i] 
            else:
                continue #Nada :P
    return L, U


def inversaLU(L, U):

    I = np.array([[1,0,0], [0,1,0], [0,0,1]]) #Identidad

    L_1 = solve_triangular(L, I, lower = True) #Resolver L.x = I, entonces x = L^-1
    U_1 = U_1 = solve_triangular(U, I)  #Analogo para U

    Inv = U_1 @ L_1
    return Inv