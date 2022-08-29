import random


opposite = {
    'NORTH': 'SOUTH',
    'EAST': 'WEST',
    'SOUTH': 'NORTH',
    'WEST': 'EAST'
}

def generate_directions():
    raw_directions = list()
    for _ in range(5):
        single_choice = random.choice(list(opposite.keys()))
        raw_directions.append(single_choice)
    return raw_directions

def cleanse_directions():
    raw_directions = generate_directions()
    print("Before:", raw_directions)
    for raw_direction in raw_directions:
        if opposite[raw_direction] in raw_directions:
            raw_directions.remove(raw_direction)
            raw_directions.remove(opposite[raw_direction])
    cleansed_directions = raw_directions
    print("After:", cleansed_directions)
    return cleansed_directions

cleanse_directions()