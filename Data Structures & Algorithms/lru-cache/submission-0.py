class Node:

    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key, self.value = key, val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.left = self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
        self.map = {}

    def insert_node(self, node: Node) -> None:
        left , right = self.left, self.left.next
        node.prev, node.next  = left, right
        left.next = right.prev = node
        
    
    def remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        print(f"get {key}")
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove_node(node)
        self.insert_node(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        print(f"put {key}, {value}")
        node = None
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.remove_node(node)
        else:
            node = Node(key=key,val=value)
            self.map[key] = node
        
        self.insert_node(node)
        
        if len(self.map) > self.capacity:
            tail = self.right.prev
            self.remove_node(tail)
            del self.map[tail.key]
        
        print(self.map)
        
    
        
