"""
Hash table for packages loaded from CSV files

This implementation uses chaining to resolve collisions,
because the input data set is known ahead of time to be small.
Searching for any key should be O(1), or nearly so, in all cases.
The structure is self-adjusting because chaining allows the structure
to grow to handle more than one object with the same hash value.

Time complexity: O(n) worst case, and O(1) average case.

Credit: C950 Webinar 1: Let's Go Hashing is the basis for this code,
 with some additional edits for my own clarity.
"""


class HashTable:
    def __init__(self, size=40):
        # Initialize an empty hash table with 10 empty
        self.table = []
        for i in range(size):
            self.table.append([])

    def get_hash_key(self, key):
        return int(key) % len(self.table)

    # Adds a package to the hash table. Updates a package if it already exists. Time complexity is O(1).
    def insert(self, key, item):
        # Determine which bucket the item should be inserted into, then get a reference to the list in that bucket
        bucket = self.get_hash_key(key)
        bucket_list = self.table[bucket]

        # If the key is already in the bucket, update the value
        for package in bucket_list:
            if package[0] == key:
                package[1] = item
                return True

        # If not, append the item to the end of bucket_list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item in the hash table. Time complexity is O(1).
    def search(self, key):
        # Get the bucket associated with the key
        bucket = self.get_hash_key(key)
        bucket_list = self.table[bucket]

        # Search for the key in the bucket_list
        for package in bucket_list:
            if package[0] == key:
                return package[1]
        return None

    # Removes an item from the hash table. Time complexity is O(1).
    def remove(self, key):
        # Get the bucket associated with the key
        bucket = self.get_hash_key(key)
        bucket_list = self.table[bucket]

        # If the item exists, remove it
        for package in bucket_list:
            if package[0] == key:
                bucket_list.remove([package[0], package[1]])
