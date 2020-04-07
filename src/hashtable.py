# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for i in key:
            hash = (hash * 33) + ord(i)
        return hash % self.capacity

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # Have key and value for this function
        # Find the index, utilizing _hash_mod
        index = self._hash_mod(key)
        # Setting node bucket
        node = self.storage[index]
        # Check the storage index
        if node is None:
            # Setting the current storage[index] to key, value
            self.storage[index] = LinkedPair(key, value)
            return
        if node is not None:
            # Setting a new node w/ key, value
            new_node = LinkedPair(key, value)
            # Moving to the next node
            new_node.next = self.storage[index]
            # Setting index to the new node
            self.storage[index] = new_node

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # Have key for this function
        # Finding the index, utilizing _hash_mod
        index = self._hash_mod(key)
        # Setting node bucket
        node = self.storage[index]
        # Setting previous value to None
        previous = None
        while node is not None and node.key != key:
            previous = node
            node = node.next
        if node is None:
            print(f"Danger, Danger, There is no key at ({index}).")
        else:
            if previous is None:
                self.storage[index] = node.next
            else:
                previous.next = node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Have key for this function
        # Finding the index, utilizing _hash_mod
        index = self._hash_mod(key)
        # Setting node bucket / storage
        node = self.storage[index]
        # If there is an item at storage[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # Only have self, similar to dynamic_array - double_size
        # Double the capacity --> self.capacity *= 2
        self.capacity *= 2
        # Saving storage
        old_storage = self.storage
        # Setting new_storage to list of none * capacity
        new_storage = [None] * self.capacity
        # Setting storage to new_storage
        self.storage = new_storage
        # Looking for items in storage
        for i in range(len(old_storage)):
            # Only if there is an item within the storage
            # New storage is created
            # Assigning the key/value pair into the new location
            if old_storage[i] is not None:
                bucket_item = old_storage[i]
                while bucket_item is not None:
                    self.insert(bucket_item.key, bucket_item.value)
                    bucket_item = bucket_item.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test Removal
    # print(ht.remove("line_1"))
    # print(ht.remove("line_4"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
