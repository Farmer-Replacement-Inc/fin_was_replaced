def carrot_square():
	if not get_ground_type() == Grounds.Soil:
		till()
	plant(Entities.Carrot)

def wood_square():
	if even_row() and not even_col():
			plant(Entities.Tree)
	elif not even_row() and even_col():
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)

def pumpkin_square():
	if not get_ground_type() == Grounds.Soil:
		till()
	plant(Entities.Pumpkin)
	while not can_harvest() and get_entity_type() == Entities.Pumpkin:
		pass
	if get_entity_type() == Entities.Dead_Pumpkin:
		pumpkin_square()
	

def even_row():
	return get_pos_y() % 2 == 0
	
def even_col():
	return get_pos_x() % 2 == 0