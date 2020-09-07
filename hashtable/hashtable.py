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
        if self.head == None:
            return None

        curr = self.head

        while(curr != None):
            if curr.key == key:
                return curr
            else:
                curr = curr.next

        return None

    def insert(self, key, value):
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node

    def remove(self, key):
        curr = self.head #We need a variable to hold the current Node
        warning = "Warning: key not found." #Our warning message

        if curr == None: #Linked List has no nodes
            print(warning)
            return

        #There is at least one node, but we can't use find because may need the prev node in order to delete

        #first we need to check if it's at the head
        if curr.key == key: #It's at the head
            #We need to disconnect it from the next pointer
            self.head = curr.next #That's it! The head pointer is completely overwritten
            #the next pointer is now the head, if next is none, table[index] is none!
            return

        #It's not at the head, we have to check elsewhere
        prev = curr #We will need to know the previous node in order to delete it
        curr = curr.next #We need a place to hold the current node in the list; it's table[index].next because we checked the head

        while(curr != None): #Go through the Linked List till you run into None
            #print(curr.key, key)
            if curr.key == key: #We found it! Now we must destroy it
                prev.next = curr.next #prev points to the next node
                curr.next = None # Got to remove all connections to and from current node, so it gets deleted
                return
            else:
                prev = curr
                curr = curr.next

        #If you get this far the key was not found
        print(warning)


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity > MIN_CAPACITY:
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY
        
        self.table = [LinkedList()] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        load_factor = 0
        for e in self.table:
            if e is not None:
                load_factor += 1
        
        return load_factor / self.capacity



    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        fnv1_hash = 14695981039346656037
        key_encoded = key.encode()
        for e in key_encoded:
            fnv1_hash = fnv1_hash * 1099511628211
            fnv1_hash = fnv1_hash ^ e

        #print(fnv1_hash)
        return fnv1_hash



    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        djb2_hash = 5381
        key_encoded = key.encode()
        for e in key_encoded:
            djb2_hash = ((djb2_hash << 5) + djb2_hash) + e
            #djb2_hash = (djb2_hash * 33) + e

        #print(djb2_hash)
        return djb2_hash
        


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key) #Get index

        node = self.table[index].find(key)#Try to find the key in the linked list, store it in node

        if node == None: #Key not found, let's insert a new one into the linked list!
            self.table[index].insert(key, value)
        else: #key found, lets override the current value
            node.value = value
    
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key) #Let's just get the index and put it here

        self.table[index].remove(key)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key) #get the index
        
        node = self.table[index].find(key) #search the linked list

        if node == None: #node is None if the key wasn't found, return None
            return None
        
        return node.value #Otherwise return the value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
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
