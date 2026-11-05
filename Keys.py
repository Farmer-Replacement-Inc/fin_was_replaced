

harvest_keys = {
Items.Carrot:Entities.Carrot,
Items.Pumpkin:Entities.Pumpkin
}

def get_entity_from_item(item):
	return harvest_keys[item]
