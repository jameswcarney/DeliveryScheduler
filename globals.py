"""
Some objects that need to be accessed globally.
Space complexity is described in files related to each data structure
"""

from hash_table import HashTable
from truck import Truck

package_hash = HashTable()
adjacency_list = []
address_list = []

truck_one = Truck(1, 8, 0, 0)
truck_two = Truck(2, 9, 20, 0)
truck_three = Truck(3, 10, 30, 00)