class DlinkedNone():
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.caches = dict()
        self.head = DlinkedNone()
        self.tail = DlinkedNone()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.caches:
            return -1
        else:
            node = self.caches[key]
            self.move_to_head(node)
            return node.value 

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.caches:
            node = DlinkedNone(key, value)
            self.caches[key] = node
            self.size += 1
            self.add_to_head(node)
            if self.size > self.capacity:
                removed = self.remove_last_node()
                self.caches.pop(removed.key)
                self.size -= 1
        else:
            node = self.caches[key]
            node.value = value
            self.move_to_head(node)
            
    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)
    
    def remove_last_node(self):
        node = self.tail.prev
        self.remove_node(node)
        return node
    
    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)