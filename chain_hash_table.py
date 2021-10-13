INITIAL_CAPACITY = 50
MAX_LOAD_FACTOR = 0.7
MIN_LOAD_FACTOR = 0.3 # Arbitrary figure. No idea if this is when to shrink existing table

class Node:
'''node class for use in chaining'''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''hash table that utilises a linked list collision resolution'''
    def __init__ (self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None for i in range(self.capacity)]

    def get_hash(self, key):
        '''simple hash function using ascii'''
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)
        return hash_sum % self.capacity # setting to mod self.capacity ensures get_hash returns
                                        # values between 0 and the size of our list.

    def rehash(self, max_min):
        '''re-hashes existing table and doubles its previous capacity'''
        NEW_CAPACITY = self.capacity * 2
        self.lf = max_min

        # TODO: figure out how to rehash existing table.
        new_hashtable = HashTable()

    def check_lf(self):
        '''checks current load factor is between 0.3 and 0.7'''
        lf = self.size / self.capacity

        if lf >= MAX_LOAD_FACTOR:
            # TODO: write wrapper to monitor rehashing time and decorate self.rehash()
            print('Load factor is greater than 0.7. Table rehashing...')
            self.rehash('max') # correct place to call rehash() ??
            return
        if lf <= MIN_LOAD_FACTOR:
            # TODO: write wrapper to monitor rehashing time and decorate self.rehash()
            print('Load factor is less than 0.3. Table rehashing...')
            self.rehash('min') # correct place to call rehash() ??
            return
        else:
            return

    def add(self, key, value):
        '''adds a new key, value pair into HashTable'''
        self.check_lf()
        self.size += 1
        hash_index = get_hash(key)

        if self.buckets[hash_index] == None:
            self.buckets[hash_index] = Node(key, value)
            return
        else:
            node = self.buckets[hash_index]
            while node.next != None:
                prev_node = node
                node = node.next
            prev_node.next = Node(key, value)
            return

    def find(self, key):
        '''finds and returns value associated with specific key'''
        hash_index = get_hash(key)
        node = self.buckets[hash_index]

        while node is not None and node.key != key:
            node = node.next
        if node is None:
            print(f"ERROR: '{key}' not found!")
            return None
        else:
            return node.value

    def delete(self, key):
        '''deletes a key, value pair from the HashTable'''
        hash_index = get_hash(key)
        node = self.buckets[hash_index]

        while node is not None and node.key != key:
            prev_node = node
            node = node.next
        if node is None:
            print(f"ERROR: '{key}' not found!")
            return None
        else:
            self.size -= 1
            # TODO: finish node deletion
            self.check_lf()


# TODO: class method: write hash function using ascii numbers
# TODO: class method: write function to add item
# TODO: class method: write function to get item
# TODO: class method: write function to delete item
# TODO: refactor to dynamic table that rehashes itself when too full or too empty



'''
# --------------------------------- NOTES ----------------------------------- #

Hash tables are used to index large amounts of data. Provides data lookup by keys
rather than by index. The data is stored via a calculated (hashed) index where the
key itself is run through a defined hash function to determine this index.

Search complexity =  O(n) worst case

Use cases:
- Used in database indexing
- Compilers
- Caching
- Password authentication

Hash algorithm/function = algorithm used to determine an index for storage or retrieval.

Load factor = no. of elements / capacity of table. Once this ratio is ~ 0.7 - 0.8, lots
of collisions can be expected and rehashing the table to increase capacity is recommended.

Collision Resolution:
Collisions occur when data is hashed to the same index as a previously hashed
data. Avoiding collisions can be done through techniques such as 'open addressing'
and 'closed addressing'...

Collision solutions:  -- Open addressing --
                         'linear probing'
                         'plus 3 rehash',
                         'quadratic probing',
                         'double hashing'

                      -- Closed addressing --
                         'chaining'

Linear probing - If the index is occupied, traverse linearly until a free element
is located to store data. This is known as 'open addressing', but can result in
'primary clustering', where keys bunch together within the array and leave other
areas largly unoccupied.

Plus 3 rehash - Similar to linear probing, but will look at every 3rd space along,
until a free index is found.

Quadratic probing - Squares the number of failed attempts when deciding how far
along from the original point of collision to look next. Each time another failed
atempt is made, the distance moved is exponential.

Double hashing - Applies a second hashing function to the key when a collision
occurs. The result of the second hashing gives the number of spaces away from the
original collision to try next.

Chaining - Each index contains a linked list. If data is hashed to an already
occupied index, this data is appended to the linked list at this index. Retrieval
of this data is done through a standard linked list traversal search once the hash
index has been determined.

An ideal hash function comprises of the following:
- Minimises collisions
- Distributes values uniformly
- Easy to calculate
- Easily resolves any collisions

'''
