# main program

# importing the functions.py,
# moveup.py and movedown.py files
import functions
import moveup
import movedown


if __name__ == '__main__':
	
# calling start_game function
# to initialize the matrix
	mat = functions.start_game()

while(True):

	for i in range (4):
		print(mat[i])

	# taking the user input
	# for next step
	x = input("Press the command : ")


	# we have to move up
	if(x == '3'):

		# call the up function from moveup
		mat = moveup.up(mat)

		# get the current state and print it
		status = functions.get_current_state(mat)
		print(status)

		# if game not over then continue
		# and add a new random 2 or 4
		if(status == 'GAME NOT OVER'):
			functions.rand_2or4(mat)

		# else break the loop
		else:
			break

	# same for remaining moves

	# to move down
	elif(x == '4'):
		mat = movedown.down(mat)
		status = functions.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			functions.rand_2or4(mat)
		else:
			break

	# to move left
	elif(x == '1'):
		mat = functions.transpose(mat)
		mat = moveup.up(mat)
		mat = functions.transpose(mat)
		status = functions.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			functions.rand_2or4(mat)
		else:
			break

	# to move right
	elif(x == '2'):
		mat = functions.transpose(mat)
		mat = movedown.down(mat)
		mat = functions.transpose(mat)
		status = functions.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			functions.rand_2or4(mat)
		else:
			break
	else:
		print("Invalid Key Pressed")

	# print the matrix after each
	# move.
	
