import csv
import globals
from package import Package


"""
Loads package data from packages.csv
Complexity: O(n), for both time and space
"""
def load_package_data(file_name):
    with open(file_name) as packages:
        package_data = csv.reader(packages, delimiter=',')
        for package in package_data:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip = package[4]
            deadline = package[5]
            weight = package[6]
            notes = package[7]
            delivery_time = ''
            location = ''
            status = "Hub"

            to_be_loaded = Package(package_id, address, city, state, zip, deadline, weight, notes, delivery_time,
                                   location, status)
            key = to_be_loaded.id
            globals.package_hash.insert(key, to_be_loaded)

            # We make some choices here about which truck a package should be loaded to
            # based on required delivery time and any special notes or delays.
            if to_be_loaded.deadline != 'EOD':
                if 'Must' in to_be_loaded.notes or 'None' in to_be_loaded.notes:
                    to_be_loaded.status = 'Hub'
                    globals.truck_one.load_package(to_be_loaded)
            if to_be_loaded.id == 19:
                to_be_loaded.status = 'Hub'
                globals.truck_one.load_package(to_be_loaded)
            if 'Can only be' in to_be_loaded.notes:
                to_be_loaded.status = 'Hub'
                globals.truck_two.load_package(to_be_loaded)
            if 'Delayed' in to_be_loaded.notes:
                to_be_loaded.status = 'Delayed'
                globals.truck_two.load_package(to_be_loaded)
            if '84104' in to_be_loaded.zip and '10:30' not in to_be_loaded.deadline:
                to_be_loaded.status = 'Hub'
                globals.truck_three.load_package(to_be_loaded)
            if 'Wrong address listed' in to_be_loaded.notes:
                to_be_loaded.address = '410 S State St'
                to_be_loaded.zip = '84111'
                to_be_loaded.status = 'Hub'
                globals.truck_three.load_package(to_be_loaded)
            if (to_be_loaded not in globals.truck_one.package_list and
                    to_be_loaded not in globals.truck_two.package_list and
                    to_be_loaded not in globals.truck_three.package_list):
                if len(globals.truck_two.package_list) > len(globals.truck_three.package_list):
                    to_be_loaded.status = 'Hub'
                    globals.truck_three.load_package(to_be_loaded)
                else:
                    to_be_loaded.status = 'Hub'
                    globals.truck_two.load_package(to_be_loaded)


"""
Loads distance data from distances.csv and stores as an adjacency list
Complexity: O(n) time, O(n^2) space
"""
def load_adjacency_data(file_name):
    with open('./data/distances.csv') as distances:
        for row in csv.reader(distances, delimiter=','):
            globals.adjacency_list.append(row)


"""
Loads a list of addresses from addresses.csv, to aid in making comparisons against the adjacency list
Complexity: O(n) time and space
"""
def load_address_data(file_name):
    with open('./data/addresses.csv') as addresses:
        for row in csv.reader(addresses, delimiter=','):
            globals.address_list.append(row[2])
