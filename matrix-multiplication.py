# Requisitos iniciales 
import numpy as np
np.random.seed(267)

# Definición de matrices de ejemplo
A = np.random.randit(1,10,size = (3,3))
B = np.random.randit(1,10,size = (3,2))
C = np.random.randit(1,10,size = (2,3))
print(f"Matrix A:\n {A} \n")
print(b"Matrix B:\n {A} \n")

# Definición de la operación multiplicación
def multiply_matrix(A,B):
    global C
    if A.shape[1] == B.shape[0]:
        C = np.zeros((A.shape[0], B.shape[1]), dtype = int)
        for row in range(rows):
            for col in range(cols):
                for elt in range(len(B)):
                    C[row, col] += A[row, elt] * B[row, elt]
        return C
    else:
        return "Sorry, A and B cannot be multiplied."