import numpy
import random as rand
import math



def makePuzzle(size, dif):
	mat = numpy.zeros((size, size))
	for i in range(0, 17 + dif):
		myBool = True
		row = -1
		col = -1
		testnum = -1
		
		while(myBool):
			myBool = False
			row = rand.randint(0,size - 1)
			col = rand.randint(0,size - 1)
			testnum = rand.randint(1, size)
			if mat[row, col] == 0:
				for x in range(0,size - 1):
					if mat[x, col] == testnum:
						myBool = True
					if mat[row, x] == testnum:
						myBool = True
				for y in range(int(math.floor(row/math.sqrt(size))*math.sqrt(size)), int(math.floor(row/math.sqrt(size))*math.sqrt(size) + 3.0)):	
					for z in range(int(math.floor(col/math.sqrt(size))*math.sqrt(size)), int(math.floor(col/math.sqrt(size))*math.sqrt(size) + 3.0)):	
						if mat[y,z] == testnum:
							myBool = True
			else:
				myBool = True
		mat[row, col] = testnum
		
	return mat

mySud = makePuzzle(9,0)
print(mySud)
mySud = makePuzzle(16,0)
print(mySud)
#mySud = makePuzzle(20,0)
#print(mySud)
