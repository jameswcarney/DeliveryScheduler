import globals
from datetime import datetime

"""
Prints the status of all packages at a user-defined time.
Complexity: O(n)
"""
def print_all_packages_at_time(time):
    for package in globals.package_hash.table:
        if package[0][1].id == 9 and time < datetime(datetime.now().year, datetime.now().month, datetime.now().day, 10, 20, 0):
            print("Package " + str(package[0][1].id) + " En Route to 300 State St, Salt Lake City, UT, 84103" + " Weight: " + package[0][1].weight)
        if (package[0][1].id == 6 or package[0][1].id == 25 or package[0][1].id == 28 or package[0][1].id == 32) and \
                time < datetime(datetime.now().year, datetime.now().month, datetime.now().day, 9, 5, 0):
            print("Package " + str(package[0][1].id) + " Delayed")
        if package[0][1].delivery_time > time:
            print("Package " + str(package[0][1].id) + " En route to " + str(package[0][1].address) + ' ' + package[0][1].city + ", " + package[0][1].state + " " + package[0][1].zip + ", Weight: " + package[0][1].weight)
        else:
            print("Package " + str(package[0][1].id) + " Delivered at " +
                  str(package[0][1].delivery_time.strftime("%H:%M:%S")) + " to " + str(package[0][1].address) + ' ' + package[0][1].city + ", " + package[0][1].state + " " + package[0][1].zip + ", Weight: " + package[0][1].weight)


"""
Prints the status of an individual package at a user-defined time.
Complexity: O(n) worst case, O(1) average
"""
def print_package_at_time(package_id, time):
    package = globals.package_hash.search(package_id)
    if package.id == 9 and time < datetime(datetime.now().year, datetime.now().month, datetime.now().day, 10, 20, 0):
        print("Package: " + str(package.id))
        print("Address: " + "300 State St, Salt Lake City, UT, 84103")
        print("Status: " + package.status)
        print("Expected delivery: " + str(package.delivery_time.strftime("%H:%M:%S")))
        print("")
        return
    if (package.id == 6 or package.id == 25 or package.id == 28 or package.id == 32) and \
            time < datetime(datetime.now().year, datetime.now().month, datetime.now().day, 9, 5, 0):
        print("Package: " + str(package.id))
        print("Address: " + str(package.address) + ", " + package.city + ", " + package.state + " " + package.zip)
        print("Status: Delayed")
        print("Expected delivery: " + str(package.delivery_time.strftime("%H:%M:%S")))
        print("")
        return
    if package.delivery_time > time:
        package.status = 'En Route'
        print("Package: " + str(package.id))
        print("Address: " + str(package.address) + ", " + package.city + ", " + package.state + " " + package.zip)
        print("Status: " + package.status)
        print("Expected delivery: " + str(package.delivery_time.strftime("%H:%M:%S")))
        print("")
    else:
        print("Package: " + str(package.id))
        print("Address: " + str(package.address) + ", " + package.city + ", " + package.state + " " + package.zip)
        print("Status: delivered at " + package.delivery_time.strftime("%H:%M:%S"))

