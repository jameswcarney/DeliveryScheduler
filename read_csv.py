import csv
from objects import Package
from hash_table import HashTable

packageHash = HashTable()


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
            packageHash.insert(package_id, package)


def load_adjacency_data(file_name):
    with open(file_name) as distances:
        adjacency_data = list(csv.reader(distances, delimiter=','))


load_package_data('./data/packages.csv')
load_adjacency_data('./data/distances.csv')


