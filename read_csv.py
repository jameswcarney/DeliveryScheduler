import csv
import globals
from objects import Package


# Load package data from packages.csv and insert it into a hash table
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
            status = "Loaded"

            package = Package(package_id, address, city, state, zip, deadline, weight, notes, status)

            # Insert the package into the hash table
            globals.packageHash.insert(package_id, package)


# Load weighted distance data from distances.csv and use it to create an adjacency list
def load_adjacency_data(file_name):
    with open(file_name) as distances:
        adjacency_data = list(csv.reader(distances, delimiter=','))
        for node in adjacency_data:
            globals.adjacency_list.append(node)


# Load address data from addresses.csv to create an address list
def load_address_data(file_name):
    with open(file_name) as addresses:
        address_data = csv.reader(addresses, delimiter=',')
        for address in address_data:
            globals.address_list.append(address[1])


load_package_data('./data/packages.csv')
load_adjacency_data('./data/distances.csv')
load_address_data('./data/addresses.csv')


