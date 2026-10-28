from replace_farmer import move_to_square
from harvest import harvest

def big_pumpkin(rows = 6, cols = 6):
	for col in range(cols):
		for row in range(rows):
			harvest()			
			plant_pumpkin()
			move_to_square(row, col)
	
def plant_pumpkin():
	if not get_ground_type() == Grounds.Soil:
		till()
	plant(Entities.Pumpkin)
	while not can_harvest:
		pass
	if get_entity_type == Entities.Dead_Pumpkin:
		plant_pumpkin()

