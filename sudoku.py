import numpy
import random as rand
import math


#this makes a random puzzle with values removed to be solved by the rest of the program
def makePuzzle(size, dif):
	mat = numpy.zeros((size, size))	#make a matrix of the correct size
	for i in range(0, 17 + dif):	#fill in a number of cells depending on difficulty you want
		myBool = True
		row = -1
		col = -1
		testnum = -1
		
		while(myBool):
			myBool = False
			row = rand.randint(0,size - 1)		#find a random number for row
			col = rand.randint(0,size - 1)		#find a random number for col
			testnum = rand.randint(1, size)		#find a random number for actual value
			if mat[row, col] == 0:				#check to see if value is in position
				for x in range(0,size - 1):
					if mat[x, col] == testnum:	#check to see if value is valid for column 	
						myBool = True
					if mat[row, x] == testnum:	#check to see if value is valid for row
						myBool = True
				for y in range(int(math.floor(row/math.sqrt(size))*math.sqrt(size)), int(math.floor(row/math.sqrt(size))*math.sqrt(size) + 3.0)):	#check to see if value is valid for square
					for z in range(int(math.floor(col/math.sqrt(size))*math.sqrt(size)), int(math.floor(col/math.sqrt(size))*math.sqrt(size) + 3.0)):	
						if mat[y,z] == testnum:
							myBool = True
			else:
				myBool = True
		mat[row, col] = testnum
		
	return mat

def needFillcells(grid, gridsize, i, j):		#this funtion is going to run through and find the next valid location to fill

	for x in range (i, gridsize):
		for y in range(j, gridsize):
			if gird[x][y] == 0:
			#may need to return tuples???
				return x,y
				
	for x in range(0, gridsize):
		for y in range(0, gridsize):
			if grid[x][y] == 0:
				return x,y
				
	return -1, -1
	
	
def isValid(grid, gridsize, i, j, e):

	rowCheck = all(e != grid[i][x], for x in range(gridsize))	#Cool little hack to check the whole row to see if the row is a valid solution
	
	if rowCheck:
		columnCheck = all(e != grid[x][j] for x in range(gridsize)
		if columnCheck:
			# finding the top left x,y co-ordinates of the section containing the i,j cell
			secTopX, secTopY =  secTopX, secTopY = 3 *(i/3), 3 *(j/3)		# may have edge cases and need some math loveing..... Chris and Marissa 
			for x in range(secTopX, secTopX + 3):
				for y in range(secTopY, secTopY + 3):
					if grid[x][y] == e:
						return False
			return True
	return False
		
def solver(grid, i = 0, j = 0):

	m,n = grid.shape
	gridsize = len(m)
	
	i, j = needFillcells(grid, gridsize, i, j)
	if i == -1:
		return True

	for e in range(1, gridsize + 1):
		if isValid(grid, gridsize, i, j, e):
			grid[i][j] = e
			if solver(grid, i, j):
				return True
			grid[i][j] = 0
	return False
		

mySud = makePuzzle(9,0)
print(mySud)
mySud = makePuzzle(16,0)
print(mySud)
#mySud = makePuzzle(20,0)
#print(mySud)
solver(mySud)
print (mySud)

