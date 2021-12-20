import globals
from package import Package
from datetime import date
from datetime import timedelta
from datetime import datetime
from distance import get_distance, get_total_distance

"""
A class representing trucks that will deliver packages
"""
class Truck:
    def __init__(self, truck_id, departure_hour, departure_minutes, departure_seconds):
        self.id = truck_id
        self.package_list = []
        self.route = []
        self.route_length = 0
        self.clock = datetime(date.today().year, date.today().month, date.today().day,
                              departure_hour, departure_minutes, departure_seconds)

    """
    Loads a package onto a truck.
    Complexity: O(1)
    """
    def load_package(self, package):
        self.package_list.append(package)

    """
    Calculates the delivery route for a truck using nearest-neighbor (greedy) algorithm.
    The algorithm starts with the first address, which is the hub. It compares against every package in the truck and
    places the one closest to the hub first. Then, it then finds the closest package address to the first delivery,
    and places it next. The algorithm repeats until all packages loaded onto the truck have been sorted. This algorithm
    is self-adjusting because any package that has already been sorted is removed from the list of items to be compared
    against in the next iteration.
    
    Complexity: O(n) 
    """
    def calc_delivery_route(self, current_location=0):
        smallest_distance = 99.0
        new_location = 0

        for package in self.package_list:
            if get_distance(current_location, globals.address_list.index(package.address)) <= smallest_distance:
                smallest_distance = get_distance(current_location, globals.address_list.index(package.address))
                new_location = globals.address_list.index(package.address)
        for package in self.package_list:
            if get_distance(current_location, globals.address_list.index(package.address)) == smallest_distance:
                self.route.append(package)
                self.package_list.pop(self.package_list.index(package))
                current_location = new_location
                self.calc_delivery_route(current_location)

    """
    Calculates the length of an optimized delivery route.
    Complexity: O(n)
    """
    def calc_route_length(self):
        for index, elem in enumerate(self.route):
            if index + 1 < len(globals.truck_one.route):
                curr_el = self.route[index]
                next_el = self.route[index + 1]

                self.route_length = get_total_distance(globals.address_list.index(curr_el.address),
                                                       globals.address_list.index(next_el.address),
                                                       self.route_length)

    """
    Calculates the delivery time for each package in an optimized delivery route.
    Complexity: O(n)
    """
    def calc_delivery_times(self):
        for index, elem in enumerate(self.route):
            if index + 1 < len(self.route):
                curr_el = self.route[index]
                next_el = self.route[index + 1]

                package_distance = get_distance(globals.address_list.index(curr_el.address),
                                                globals.address_list.index(next_el.address))

                package_delivery_time_hours = package_distance / 18  # Truck speed is 18mp/h
                delta_hours = int(package_delivery_time_hours)
                delta_minutes = (package_delivery_time_hours * 60) % 60
                delta_seconds = (package_delivery_time_hours * 3600) % 60
                new_time = self.clock + timedelta(hours=delta_hours, minutes=delta_minutes,
                                                  seconds=delta_seconds)
                self.clock = new_time
                next_el.delivery_time = new_time
                next_el.status = "Delivered"
                globals.package_hash.insert(next_el.id, next_el)

    """
    Prints a delivery route. Used only for debugging.
    Complexity: O(n)
    """
    def print_delivery_route(self):
        for node in self.route:
            if node.id == 0 or node.id == 41:
                pass
            else:
                print("Package #" + str(node.id) + " Status - " + str(node.status))

    """
    Runs several functions that prepare a truck for departure.
    Complexity: O(n), because none of the subroutines are greater than O(n).
    """
    def prepare_truck_departure(self):
        self.route.insert(0, Package(0, "4001 South 700 East", "Salt Lake City", "UT", "84107", "Never", 0,
                                     "Fake Package for Start and End", '', '', 'Placeholder'))
        print("Truck " + str(self.id) + ", departing at: " + str(self.clock.strftime("%H:%M:%S")))
        print("-------------------------------")
        self.calc_delivery_route()
        self.route.append(Package(41, "4001 South 700 East", "Salt Lake City", "UT", "84107", "Never", 0,
                                  "Fake Package for Route End", '', '', 'Placeholder'))
        # self.print_delivery_route()
        self.calc_delivery_times()
        self.calc_route_length()
        print("Returning to hub at: " + str(self.clock.strftime("%H:%M:%S")))
        print("Route distance: " + str("{:.2f}".format(self.route_length)) + " miles.")
        print("")


