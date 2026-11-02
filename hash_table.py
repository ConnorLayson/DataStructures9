class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = Contact(key, value)
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def print_table(self):
        for i, contact in enumerate(self.data):
            if contact:
                print(f"Index {i}: {contact.value}")
            else:
                print(f"Index {i}: Empty")

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        current =  self.data[index]
        if self.data[index] is None:
            self.data[index] = Node(key, value)
            return

        while current:
            if current.key == key:
                current.value = value
                return

            if current.next is None: 
                break
            
            current = current.next
                
            current.next = Node(key, value)
    
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        return None

# Test your hash table implementation here.  
table = HashTable(10)
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
# Print the new table structure 
table.print_table()