# Author: James Carney || Student ID: 003436494
# Code execution screenshots are in the /screenshots subdirectory of the project
import globals
import data_views
from datetime import datetime
from datetime import date
from read_csv import load_package_data
from read_csv import load_adjacency_data
from read_csv import load_address_data

"""
Main function of WGUPSDeliveryScheduler
"""
def main():
    load_package_data('./data/packages.csv')
    load_adjacency_data('./data/distances.csv')
    load_address_data('./data/addresses.csv')

    globals.truck_one.prepare_truck_departure()
    globals.truck_two.prepare_truck_departure()
    globals.truck_three.prepare_truck_departure()
    total_distance = globals.truck_one.route_length + globals.truck_two.route_length + globals.truck_three.route_length
    print("Total distance for all trucks: " + str(total_distance) + " miles.")
    print("")

    input_time = input("Enter a time in the format HH:MM:SS to see the status of all packages: ").split(":")
    time = datetime(date.today().year, date.today().month, date.today().day, int(input_time[0]), int(input_time[1]),
                    int(input_time[2]))
    data_views.print_all_packages_at_time(time)



if __name__ == "__main__":
    main()
