import csv
from objects import Package
from hash_table import HashTable

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

packageHash = HashTable()

load_package_data('./data/packages.csv')

for i in range(len(packageHash.table)):
    print("Key: {} and Package: {}".format(i+1, packageHash.search(i+1)))



