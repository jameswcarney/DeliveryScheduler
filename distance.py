import globals


def get_distance(location_one, location_two):
    distance = globals.adjacency_list[location_one][location_two]
    if distance == '':
        distance = globals.adjacency_list[location_two][location_one]
    return float(distance)


def get_total_distance(location_one, location_two, total):
    distance = globals.adjacency_list[location_one][location_two]
    if distance == '':
        distance = globals.adjacency_list[location_two][location_one]

    total += float(distance)
    return float(total)


def nearest_neighbor(packages, truck, current_location):
    if len(packages) == 0:
        return packages
    else:
        smallest_distance = 99.0
        new_location = 0
        for package in packages:
            if get_distance(current_location, globals.address_list.index(package[2])) <= smallest_distance:
                smallest_distance = get_distance(current_location, globals.address_list.index(package[2]))
                new_location = globals.address_list.index(package[2])
        for package in packages:
            if truck == 1:
                if get_distance(current_location, globals.address_list.index(package[2])) == smallest_distance:
                    globals.truck_one_opt.append(package)
                    globals.truck_one_index.append(package)
                    packages.pop(packages.index(package))
                    current_location = new_location
                    nearest_neighbor(packages, 1, current_location)
            if truck == 2:
                if get_distance(current_location, globals.address_list.index(package[2])) == smallest_distance:
                    globals.truck_two_opt.append(package)
                    globals.truck_two_index.append(package)
                    packages.pop(packages.index(package))
                    current_location = new_location
                    nearest_neighbor(packages, 2, current_location)
            if truck == 3:
                if get_distance(current_location, globals.address_list.index(package[2])) == smallest_distance:
                    globals.truck_three_opt.append(package)
                    globals.truck_three_index.append(package)
                    packages.pop(packages.index(package))
                    current_location = new_location
                    nearest_neighbor(packages, 3, current_location)


def calc_delivery_order():
    nearest_neighbor(globals.truck_one_packages, 1, 0)
    nearest_neighbor(globals.truck_two_packages, 2, 0)
    nearest_neighbor(globals.truck_three_packages, 3, 0)


