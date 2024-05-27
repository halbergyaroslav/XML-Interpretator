class RootNode:
    def __init__(self, tacs):
        self.name = None
        self.tacs = tacs
   
    
class Node:
    def __init__(self):
        self.opcode = None
        self.order = None
        self.dst = None
        self.src1 = None
        self.src2 = None
    
        
class Src:
    def __init__(self):
        self.type = None
        self.value = None
    
        
class Element():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        new_element = Element(data)
        
        if self.tail is None:
            self.head = new_element
            self.tail = new_element
            return
        
        else:
            self.tail.next = new_element
            new_element.prev = self.tail
            self.tail = self.tail.next
    
            