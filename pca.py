
import math
import numpy as np
import matplotlib.pyplot as plt

def dot(vec1, vec2):
    size = len(vec1)
    s = 0
    for i in range(size):
        s += vec1[i] * vec2[i]
    return s

def magnitude(vector):
    s = 0
    for x in vector:
        s += x*x
    return round(math.sqrt(s), 3)

def normalize_vector(vec):
    res = []
    size = len(vec)
    mag = magnitude(vec)
    for i in range(size):
        res.append( vec[i] / mag)
    return res

def matrix_equal(mat1, mat2):
    size = len(mat1)
    equal = True
    precision = 0.1
    for i in mat1:
        for j in mat2:
            if abs( round(i -j, 3) ) > precision:
                return False
    return True

def cov(x, y, xb, yb):
	n = len(x)
	temp = 0.0	
	for i in range(n):
		temp += (x[i] -xb)*(y[i]-yb)
	return temp/(n-1)


def covmat(x,y):
	n = len(x)
	xbar = ybar = 0.0
	for i in range(n):
		xbar += x[i]
		ybar += y[i]
	xbar = xbar/n
	ybar = ybar/n
	matrix = np.arange(4, dtype='float32').reshape(2,2)
	matrix[0][0] = cov(x,x,xbar,xbar)
	print(cov(x,x,xbar,xbar))
	matrix[0][1] = cov(x,y,xbar,ybar)
	matrix[1][0] = cov(y,x,ybar,xbar)
	matrix[1][1] = cov(y,y,ybar,ybar)
	print(matrix[0][0])
	return matrix

def eigen(mat):
	diff = np.array([[1],[1]])
	lyam = np.array([[1],[0]])
	iter = 100	
	while True:
		temp = mat.dot(lyam) 
		egval = abs(temp.max());
		temp = [ (x/egval) for x in temp ]
		if matrix_equal(temp, lyam) or iter<1:
            		break	
		lyam = temp;
		iter -= 1;
	lyam = normalize_vector(lyam) 	#normal eigen vector
	return egval, lyam

def project(x,y, vec):
    size = len(x)
    res = []
    for i in range(size):
        p = [x[i], y[i]]
        dot_product = dot(vec, p)
        mag1 = magnitude(vec)
        mag2 = magnitude(p)
        cosine = dot_product / (mag1 * mag2)
        proj_len = cosine * mag2

        proj_point = ( proj_len * vec[0] / mag1, proj_len * vec[1] / mag1)
        res.append(proj_point)
    return res

def main():
	x = [1, 4, 6, 3, 7, 9, 2, 6, 3, 8]
	y = [2, 6, 1, 7, 3, 6, 7, 3, 2, 8]
	mat = covmat(x,y)
	print(mat)
	egn_val, egn_vec = eigen(mat)
	print(egn_val, egn_vec)
	result = project(x, y, egn_vec)
	print(result)
	plt.plot(x,y,'ro')
	px, py = zip(*result)
	plt.scatter(px,py)
	plt.show()


if __name__=="__main__":
	main()
