from doubly_linked_list import DoublyLinkedList
from collections import OrderedDict

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # the max number of nodes it can hold
        self.limit = limit
        # the current number of nodes it is holding
        self.size = 0
        # a doubly-linked list that holds the key-value entries
        self.doubly_linked_list = DoublyLinkedList()
        # a storage dict that provides fast access to every node stored in the cache.
        self.storage_dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage_dict:
            self.doubly_linked_list.move_to_front(self.storage_dict[key])
            return self.storage_dict[key].value[1]
        else:
            return

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage_dict:
            self.storage_dict[key].value = (key, value)
            self.doubly_linked_list.move_to_front(self.storage_dict[key])
        else:
            if self.size < self.limit:
                self.doubly_linked_list.add_to_head((key, value))
                self.storage_dict[key] = self.doubly_linked_list.head
                self.size += 1
            elif self.size >= self.limit:
                self.doubly_linked_list.add_to_head((key, value))
                self.storage_dict[key] = self.doubly_linked_list.head
                oldest_key = self.doubly_linked_list.remove_from_tail()
                self.storage_dict.pop(oldest_key[0])

#    [head] -> [node] -> [node] -> [tail]
# [mostRecent] ------------------- [LRU]