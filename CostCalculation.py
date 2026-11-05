from Keys import harvest_keys, get_entity_from_item

goal_crop = Items.Pumpkin
goal_amount = 64*10000

def can_plant(goal_crop, goal_amount):
	#goal_crop: Items object"""
	#goal_amount: int
	#returns: bool
	if goal_crop in harvest_keys:
		cost = get_cost(get_entity_from_item(goal_item))
		for key in cost:
			cost[key] *= goal_amount
		for key in cost:
			if num_items(key) >= cost[key]:
				return True
			else:
				return False
	elif goal_crop in [Items.Wood,Items.Hay]:
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

def plant_crop(goal_crop, goal_amount = 1):
	if can_plant(goal_crop, goal_amount):
		build_farm_plan()
		
def build_farm_plan(items):
	farm_size = get_world_size()
	
	
plant_crop(Items.Pumpkin, 2)


unlock_cost = get_cost(Unlocks.Expand)
#for item in unlock_cost:
#	plant_crop(item, unlock_cost[item])
