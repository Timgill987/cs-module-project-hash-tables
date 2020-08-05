class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return current

    def update_or_else_insert_at_head(self, key, value):
        # check if the key is already in the linked list
            # find the node
        current = self.head
        while current is not None:
            # if key is found, change the value
            if current.key == key:
                current.value = value
                # exit function immediately
                return
            current = current.next

        # if we reach the end of the list, it's not here!
        # make a new node, and insert at head
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node

    def del_element(self, hashTableEntry):
        current = self.head
        if current == hashTableEntry:
            self.head = self.head.next
            del hashTableEntry
            return
        while current.next != hashTableEntry:
            current = current.next
        current.next = hashTableEntry.next
        del hashTableEntry


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.count = 0
# set capacity and table to empty
        self.capacity = capacity
        # self.hashTable = [None] * capacity
        self.hashTable = [LinkedList()] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.hashTable)
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count / self.capacity
        # will return in decimal form of how full the capacity is.
        # Your code here


    # def fnv1(self, key):
    #     """
    #     FNV-1 Hash, 64-bit

    #     Implement this, and/or DJB2.
    #     """

    #     # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key: # x is a character , key is the string
            hash = (( hash << 5) + hash) + ord(x) #shifting 5 bits to the left, adding hash value, chaning the character value into an int value.
            hash &= 0xFFFFFFFF # hash after making a random number out of it.
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """



        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        #setting the specified index to the user given value
        self.hashTable[index].update_or_else_insert_at_head(key, value)
        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        #setting the value of the given index to none effectivly deleteing the index/value

        HashTableEntry = self.hashTable[self.hash_index(key)].find(key)
        if HashTableEntry is None:
            print('Key: '+key+' does not exist')
            return
        self.hashTable[self.hash_index(key)].del_element(HashTableEntry)
        # index = self.hash_index(key)
        # self.hashTable[index].find(key)
        # Your code here


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        entry = self.hashTable[index].find(key)
        if entry is not None:
            return entry.value
        return None

        # Your code here


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        oldTable = self.hashTable
        self.hashTable = [LinkedList()] * self.capacity


        for i in oldTable:
            current = i.head

            while current is not None:
                # print("putting key/value", current.key, current.value)
                self.put(current.key, current.value)
                current = current.next


        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
