import globals

"""
Calculates the distance between two addresses
Complexity: O(1)
"""
def get_distance(location_one, location_two):
    distance = globals.adjacency_list[location_one][location_two]
    if distance == '':
        distance = globals.adjacency_list[location_two][location_one]
    return float(distance)

"""
Calculates the total distance of a delivery route. Used recursively in the Truck class.
Complexity: O(n), for n packages in a delivery route.
"""
def get_total_distance(location_one, location_two, total):
    distance = globals.adjacency_list[location_one][location_two]
    if distance == '':
        distance = globals.adjacency_list[location_two][location_one]

    total += float(distance)
    return float(total)