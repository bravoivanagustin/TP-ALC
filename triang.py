import numpy as np

#sos un nazi, le llegas a mostrar esto a pablo y le da un acv

def triangular(A): 
    M = np.copy(A)
    M = M.astype(float)
    for i in range(0, min([len(M), len(M[0])])):
        p = M[i][i]
        for j in range(i+1, len(M)):
            if p != 0:
                M[j] = M[j] - (M[i]*(M[j][i]/p))
            elif M[j][i] != 0:
                B = np.copy(M[i])
                M[i] = M[j]
                M[j] = B
                p = M[i][i]
            else:
                continue
    return M

A = np.array([[0,1,0],[1,0,6], [1,2,4]])
print(A)
print(triangular(A))