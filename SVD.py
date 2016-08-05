import math 
import numpy as np
from numpy import linalg as LA

def SVD(mat):
	matT = mat.transpose()
	matmatT = mat.dot(matT)
	matTmat = matT.dot(mat)
	egnvalU, egnvecU = LA.eigh(matmatT)
	egnvalV, egnvecV = LA.eigh(matTmat)
	V = np.fliplr(egnvecV)
	VT = V.transpose()
	egnvalV = egnvalV[::-1]
	S = np.zeros(mat.shape)
	for i in range(min(mat.shape)):
		S[i][i] = math.sqrt(egnvalV[i])
	U = np.dot(np.dot(mat,np.transpose(VT)),LA.pinv(S))
	return U, S, VT

def reduceDim(u,s,v,num):
	for i in range(num):
		s = np.delete(s, s.shape[1]-1, axis = 1)
		v = np.delete(v, v.shape[0]-1, axis = 0)
		v = np.delete(v, v.shape[1]-1, axis = 1)
	return u, s, v
		

def main():
	mat = np.random.rand(5, 5)
	u, s, v = SVD(mat)
	print "Original = ", mat, "\n\nU = ",u,"\n\nS = ",s,"\n\nV =", v
	U, S, V = reduceDim(u,s,v, 3)
#	print "\nAfter Reduction of Dimension\n\n"
	red = np.dot(np.dot(U,S),V)
#	print "U = ",u,"\n\nS = ",s,"\n\nV =", v, "\n\nReformed =", red	
	
if __name__=="__main__":
	main()
