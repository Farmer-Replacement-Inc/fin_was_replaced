from harvest import harvest_square
from irrigation import water_square
from plant import carrot_square, wood_square, pumpkin_square

def replace_farmer():
	while True:
		size = get_world_size() - 1
		pumpkin = [0,1,2,3,4,5]
		carrot = [6]
		wood = [7]
		harvest_square()
		## determine where you are
		if get_pos_x() in pumpkin:
			pumpkin_square()
		if get_pos_x() in carrot:
			carrot_square()
		elif get_pos_x() in wood:
			wood_square()
		water_square()
		if get_pos_y() == size:
			if get_pos_x() == size:
				pet_the_piggy()
	
			move(East)
		move(North)

def move_to_square(new_x=0, new_y=0):
	x = new_x - get_pos_x() 
	y = new_y - get_pos_y()
	move_x(x)
	move_y(y)

def move_x(x):
	if x < 0:
		for i in range(x * -1):
			move(West)
	elif x > 0:
		for i in range(x):
			move(East)

def move_y(y):
	if y < 0:
		for i in range(y * -1):
			move(South)
	elif y > 0:
		for i in range(y):
			move(North)