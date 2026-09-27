class Node:
    def __ini__(self,key="",value=0):
        self.key = key
        self.value = value
        self.is_empty = True

class Hash_table:
    def __init__(self, size=10):
        self.size = size
        self.table = [Node() for _ in range(self.size)]

    def hashing(self, key):
        hash_val = 0
        for c in key:
            hash_val += ord(c)
        return hash_val%self.size

    def insert(self,key,value):
        index =self.hashing(key)
        self.table[index].key = key
        self.table[index].value = value
        self.table[index].is_empty = False

    def get(self, key):
        index = self.hashing(key)
        if not self.table[index].is_empty and self.table[index].key == key:
            return sel.table[index].value
        return None