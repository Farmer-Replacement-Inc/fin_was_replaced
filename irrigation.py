waterables = [
	Entities.Carrot, 
	Entities.Pumpkin]

def water_square():
	if get_entity_type() in waterables:
		if get_water() < 0.5 and num_items(Items.Water) > 0:
			use_item(Items.Water)