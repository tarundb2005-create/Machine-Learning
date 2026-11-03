import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

add = np.add(A,B)

mult = np.dot(A , B)

transpose = A.T

inverse = np.linalg.inv(A)

print("Matrix A : \n",A)
print("Matrix B : \n",B)
print("Matrix Addition: \n" , add)
print("Matrix Multiplication : \n",mult)
print("Matrix Transpose : \n",transpose)
print("Matrix Inverse : \n" , inverse)
