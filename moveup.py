x=[[0,0,4,0],[2,2,2,0],[2,2,2,4],[2,0,0,2]]

newx = []
for k in range (4):
	newx.append([0]*4)

# to compress the grid before merging cells
for j in range (4):
	pos = 0
	for i in range (4):
		if x[i][j] != 0:
			newx[pos][j] = x[i][j]
			pos += 1

# merging the cells
# take sum 
for j in range (4):
	for i in range (3):
		if newx[i][j] == newx[i+1][j] :
			newx[i][j] *= 2
			newx[i+1][j] = 0

newxx= []
for k in range (4):
	newxx.append([0]*4)

# to compress the grid after merging cells
for j in range (4):
	pos = 0
	for i in range (4):
		if newx[i][j] != 0:
			newxx[pos][j] = newx[i][j]
			pos += 1

for i in range (4):
	print (newxx[i])