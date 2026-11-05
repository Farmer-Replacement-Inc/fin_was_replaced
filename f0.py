from replace_farmer import move_to_square

def get_plant_map(x, y, xmax, ymax):	
	to_plant = []
	for col in range(x, xmax):
		if col % 2 == 0:
			for row in range(y,ymax + 1):
				to_plant.append((col, row))
		else:
			for row in range(ymax, y-1, -1):
				to_plant.append((col, row))
	return to_plant

def pumpkin_rectangle(x, y, xmax, ymax):
	to_plant = get_plant_map(x,y,xmax,ymax)
	while len(to_plant) > 0:
		finished = []
		for pos in to_plant:
			move_to_square(pos)
			if pumpkin_square():
				finished.append(pos)
		for pos in finished:
			to_plant.remove(pos)
	harvest()
			
def pumpkin_square():	
	if not get_ground_type() == Grounds.Soil:
		till()
	if get_entity_type() == Entities.Pumpkin and can_harvest():
		return True
	elif get_entity_type() == Entities.Pumpkin:	
		return False
	elif get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
		return False
	else:
		harvest()
		plant(Entities.Pumpkin)
		return False

clear()
while True:
	pumpkin_rectangle(0,0,12,11)
