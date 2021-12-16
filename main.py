import distance
import globals
from read_csv import load_package_data
from read_csv import load_adjacency_data
from read_csv import load_address_data


def main():
    load_package_data('./data/packages.csv')
    load_adjacency_data('./data/distances.csv')
    load_address_data('./data/addresses.csv')

    distance.calc_delivery_order()

    # print("Truck 1:")
    # print(globals.truck_one_opt)
    # print(len(globals.truck_one_opt))
    # print("Truck 2:")
    # print(globals.truck_two_opt)
    # print(len(globals.truck_two_opt))
    # print("Truck 3:")
    # print(globals.truck_three_opt)
    # print(len(globals.truck_three_opt))

    # Inserting dummy packages that represent the Hub as the starting/ending point for each truck
    globals.truck_one_index.insert(0, [999, '', '4001 South 700 East', 'Salt Lake City', 'UT', 84107, '', '', '', '' ])
    globals.truck_one_index.append([999, '', '4001 South 700 East', 'Salt Lake City', 'UT', 84107, '', '', '', ''])
    globals.truck_two_index.insert(0, [999, '', '4001 South 700 East', 'Salt Lake City', 'UT', 84107, '', '', '', ''])
    globals.truck_two_index.append([999, '', '4001 South 700 East', 'Salt Lake City', 'UT', 84107, '', '', '', ''])
    globals.truck_three_index.insert(0, [999, '', '4001 South 700 East', 'Salt Lake City', 'UT', 84107, '', '', '', ''])
    globals.truck_three_index.append([999, '', '4001 South 700 East', 'Salt Lake City', 'UT', 84107, '', '', '', ''])

    for index, elem in enumerate(globals.truck_one_index):
        if index + 1 < len(globals.truck_one_index):
            curr_el = globals.truck_one_index[index]
            next_el = globals.truck_one_index[index+1]

            globals.truck_one_total_distance = distance.get_total_distance(globals.address_list.index(curr_el[2]),
                                                                           globals.address_list.index(next_el[2]),
                                                                           globals.truck_one_total_distance)

    print("Truck 1 distance: ")
    print(globals.truck_one_total_distance)


    for index, elem in enumerate(globals.truck_two_index):
        if index + 1 < len(globals.truck_two_index):
            curr_el = globals.truck_two_index[index]
            next_el = globals.truck_two_index[index+1]

            globals.truck_two_total_distance = distance.get_total_distance(globals.address_list.index(curr_el[2]), globals.address_list.index(next_el[2]),
                                                                           globals.truck_two_total_distance)

    print("Truck 2 distance: ")
    print(globals.truck_two_total_distance)

    for index, elem in enumerate(globals.truck_three_index):
        if index + 1 < len(globals.truck_three_index):
            curr_el = globals.truck_three_index[index]
            next_el = globals.truck_three_index[index+1]

            globals.truck_three_total_distance = distance.get_total_distance(globals.address_list.index(curr_el[2]),
                                                                           globals.address_list.index(next_el[2]),
                                                                           globals.truck_three_total_distance)

    print("Truck 3 distance: ")
    print(globals.truck_three_total_distance)


if __name__ == "__main__":
    main()
