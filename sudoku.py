import numpy
import random as rand
import math


#this makes a random puzzle with values removed to be solved by the rest of the program
def makePuzzle(size, dif):
	sqrtn = int(math.sqrt(size))
	mat = numpy.zeros((size, size))	#make a matrix of the correct size
	minNums = 2 * size - 1 + dif
	for i in range(0, minNums):	#fill in a number of cells depending on difficulty you want
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
				for x in range(0, size):
					if mat[x, col] == testnum:	#check to see if value is valid for column 	
						myBool = True
					if mat[row, x] == testnum:	#check to see if value is valid for row
						myBool = True
				for y in range(int(math.floor(row/math.sqrt(size)) * math.sqrt(size)), int(math.floor(row/math.sqrt(size)) * math.sqrt(size) + sqrtn)):	#check to see if value is valid for square
					for z in range(int(math.floor(col/math.sqrt(size)) * math.sqrt(size)), int(math.floor(col/math.sqrt(size)) * math.sqrt(size) + sqrtn)):	
						if mat[y,z] == testnum:
							myBool = True
			else:
				myBool = True
		mat[row, col] = testnum
		
	return mat

def needFillcells(grid, gridsize, i, j):		#this funtion is going to run through and find the next valid location to fill
	
	#this is going forward checking from the i, j location to see if it can be filled optimized
	for x in range (i, gridsize):
		for y in range(j, gridsize):
			#returns the location x, y that needs filled
			if grid[x][y] == 0:
				return x,y
	#starting from the begginging and checking
	for x in range(0, gridsize):
		for y in range(0, gridsize):
			if grid[x][y] == 0:
				return x,y
				
	return -1, -1
	
#this is going to check to see if the location is a valid place to put a number
def isValid(grid, gridsize, i, j, e):
	sqrtn = int(math.sqrt(gridsize)) #this is done to make sure that we go back to the upper left corner coordinates (actually moved later, but this number is what we use)
	rowCheck = all([e != grid[i][x] for x in range(gridsize)])	#This will check an entire row and see if that row has a value
	if rowCheck:
		columnCheck = all([e != grid[x][j] for x in range(gridsize)])	#This will check an entire row and see if that column has a value

		if columnCheck:
		# finding the top left x,y co-ordinates of the section containing the i,j cell use the number found in sqrtn
			secTopX, secTopY = sqrtn *math.floor(i/sqrtn), sqrtn *math.floor(j/sqrtn) 
			#going to check the quadren and see if that is ok
			for x in range(int(secTopX), int(secTopX) + sqrtn):	
				for y in range(int(secTopY), int(secTopY) + sqrtn):	
					if grid[x][y] == e:
						return False
			return True
	return False
		
def solver(grid, i = 0, j = 0):

	#this is used to pass into all of the functions so we can change board size
	m,n = grid.shape
	gridsize = m
	
	#give me the next coord needing filled
	i, j = needFillcells(grid, gridsize, i, j)
	if i == -1:
		return True
	#Give me the next value that i can try
	for e in range(1, gridsize + 1):
		#check if that number would be valid
		if isValid(grid, gridsize, i, j, e):
			#Set that value if it is valid
			grid[i][j] = e
			if solver(grid, i, j):
				return True
			grid[i][j] = 0
	return False
		

mySud = makePuzzle(9,0)
print(mySud)
#mySud = makePuzzle(16,0)
#print(mySud)
#mySud = makePuzzle(20,0)
#print(mySud)
solver(mySud)
print (mySud)

#got it

