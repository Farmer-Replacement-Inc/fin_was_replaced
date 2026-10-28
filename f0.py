print(Items)

goal_crop = Entities.Pumpkin
goal_amount = 64*10000

def can_plant_l(goal_crop, goal_amount):
	#goal_crop: Items object"""
	#goal_amount: int
	#returns: bool
	if num_items(goal_crop) >= goal_amount:
		return True
	else:
		return False

def calc_costs(goal_crop, goal_amount):
	cost = get_cost(goal_crop)
	for key in cost:
		cost[key] *= goal_amount
		if num_items(key) < cost[key]:
			cost[key] -= num_items(key)
		else:
			cost[key] = 0
	return cost

while not can_plant(Items.Carrot, 6*60000):
	print(calc_costs(Entities.Carrot, 6*6000))

