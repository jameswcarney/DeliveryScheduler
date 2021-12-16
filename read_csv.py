import csv
import globals


# Load package data from packages.csv and insert it into a hash table
# We make some choices here about which truck a package should be loaded to
# based on required delivery time and any special notes or delays
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
            start = ''
            location = ''
            status = "Hub"

            key = package_id
            to_be_loaded = [package_id, location, address, city, state, zip, deadline, weight, notes, start, location, status]

            # We make some choices here about which truck a package should be loaded to
            # based on required delivery time and any special notes or delays.
            # We should probably do this in a load_trucks script, but it goes here for now.

            if to_be_loaded[6] != 'EOD':
                if 'Must' in to_be_loaded[8] or 'None' in to_be_loaded[8]:
                    globals.truck_one_packages.append(to_be_loaded)
            if 'Can only be' in to_be_loaded[8]:
                globals.truck_two_packages.append(to_be_loaded)
            if 'Delayed' in to_be_loaded[8]:
                globals.truck_two_packages.append(to_be_loaded)
            if '84104' in to_be_loaded[5] and '10:30' not in to_be_loaded[6]:
                globals.truck_three_packages.append(to_be_loaded)
            if 'Wrong address listed' in to_be_loaded[8]:
                to_be_loaded[2] = '410 S State St'
                to_be_loaded[5] = '84111'
                globals.truck_three_packages.append(to_be_loaded)
            if (to_be_loaded not in globals.truck_one_packages and
                    to_be_loaded not in globals.truck_two_packages and
                    to_be_loaded not in globals.truck_three_packages):
                if len(globals.truck_two_packages) > len(globals.truck_three_packages):
                    globals.truck_three_packages.append(to_be_loaded)
                else:
                    globals.truck_two_packages.append(to_be_loaded)

            globals.package_hash.insert(key, to_be_loaded)


def load_adjacency_data(file_name):
    with open('./data/distances.csv') as distances:
        for row in csv.reader(distances, delimiter=','):
            globals.adjacency_list.append(row)


def load_address_data(file_name):
    with open('./data/addresses.csv') as addresses:
        for row in csv.reader(addresses, delimiter=','):
            globals.address_list.append(row[2])








