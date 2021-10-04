def up(mat):
	newmat = []
	for k in range (4):
		newmat.append([0]*4)

	# to compress the grid before merging cells
	for j in range (4):
		pos = 0
		for i in range (4):
			if mat[i][j] != 0:
				newmat[pos][j] = mat[i][j]
				pos += 1

	# merging the cells
	# take sum 
	for j in range (4):
		for i in range (3):
			if newmat[i][j] == newmat[i+1][j] :
				newmat[i][j] *= 2
				newmat[i+1][j] = 0

	for k in range (4):
		mat[k] = [0,0,0,0]

	# to compress the grid after merging cells
	for j in range (4):
		pos = 0
		for i in range (4):
			if newmat[i][j] != 0:
				mat[pos][j] = newmat[i][j]
				pos += 1

	for i in range (4):
		print (mat[i])