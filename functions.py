import random

# function to initialize game / grid
# at the start
def start_game():

	# declaring an empty list then
	# appending 4 list each with four
	# elements as 0.
	mat =[]
	for i in range(4):
		mat.append([0] * 4)

	# printing controls for user
	print("Commands : ")
	print("1 : Move Left")
	print("2 : Move Right")
	print("3 : Move Up")
	print("4 : Move Down")

	# calling the function twice to 
	# intialize two random cells
	# with random 2 or 4
	rand_2or4(mat)
	rand_2or4(mat)

	return mat

# function to add a new 2 or 4 in
# grid at any random empty cell
def rand_2or4(mat):

# choosing a random index for
# row and column.
	r = random.randint(0, 3)
	c = random.randint(0, 3)

	count = 0

	# check if the cell is empty (0)
	# else select new random cell
	while(mat[r][c] != 0):
		r = random.randint(0, 3)
		c = random.randint(0, 3)
		count += 1
		if count > 16:
			print ("Invalid move.. Try different move..")
			return

	
	l = [2,4]
	# add a 2 or 4 to the 
	# selected random empty cell
	mat[r][c] = random.choice(l)


#function to get transpose of the matrix
def transpose(mat):
	new_mat = []
	for i in range(4):
		new_mat.append([])
		for j in range(4):
			new_mat[i].append(mat[j][i])
	return new_mat



# function to get the current
# state of game
def get_current_state(mat):
 
    # if any cell contains
    # 2048 we have won
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 2048):
                for row in mat:
                    print(row)
                return 'WON'
 
    # if we are still left with
    # atleast one empty cell
    # game is not yet over
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 0):
                return 'GAME NOT OVER'
 
    # or if no cell is empty now   
    # but if after any move left, right,
    # up or down, if any two cells
    # gets merged they will create an empty
    # cell and in that case game is not yet over
    for i in range(3):
        for j in range(3):
            if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]):
                return 'GAME NOT OVER'

    # checking the same for last 2 columns
    for j in range(3):
        if(mat[3][j]== mat[3][j + 1]):
            return 'GAME NOT OVER'
    #checking the same for last 2 rows
    for i in range(3):
        if(mat[i][3]== mat[i + 1][3]):
            return 'GAME NOT OVER'
 
    # else we have lost the game
    return 'LOST'