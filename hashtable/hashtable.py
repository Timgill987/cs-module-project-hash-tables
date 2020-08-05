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
        #while current is not None
        while current is not None:
            #if the current's key is equal to the key we're looking for
            if current.key == key:
                #return the value
                return current
            # move to the next item otherwise
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
        # base case to check if the first element == to hashtableentry
        if current == hashTableEntry:
            self.head = self.head.next
            del hashTableEntry
            return
            # while the next element isn't hashTableEntry, we move one to the right
        while current.next != hashTableEntry:
            current = current.next
        # delete hashtable entry
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
        # monitoring the percentage of what is in the hash table
        # works with resize function
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
        #setting the specified Node to a new value if the key exist
        self.hashTable[index].update_or_else_insert_at_head(key, value)
        # as the put function is loading the hash table, if the capacity gets to 70%, we double the size of the has table
        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        #setting the node to delete to the specified key of the hashtable index
        # and setting it to the key of the LL within the hashtable
        HashTableEntry = self.hashTable[self.hash_index(key)].find(key)
        # if the specified node is None
        # we don't delete anything because there is nothing there
        if HashTableEntry is None:
            print('Key: '+key+' does not exist')
            return
        # otherwise we are deleteing it.
        self.hashTable[self.hash_index(key)].del_element(HashTableEntry)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #setting index variable to the hash_index function to find the given key
        index = self.hash_index(key)
        # searching for the correct node (hashtableentry)
        entry = self.hashTable[index].find(key)
        # if node is not None
        if entry is not None:
            #return what we found
            return entry.value
        # else return none
        return None

        # Your code here


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        # declaring old hash table to copy over into new bigger one
        oldTable = self.hashTable
        # default size of the current hash table
        self.hashTable = [LinkedList()] * self.capacity

        # iterating through old table
        for i in oldTable:
            #starting at the first index
            current = i.head
            #while each index is not None
            while current is not None:
                # print("putting key/value", current.key, current.value)
                #push all contents into new hash table, The rest happens in the put function (scroll up)
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
