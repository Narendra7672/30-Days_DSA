# LRU Cache:

from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
# Test the implementation
cache = LRUCache(2)
cache.put(1, 10)
cache.put(2, 20)
print(cache.get(1))  # 10
cache.put(3, 30)
print(cache.get(2))  # -1
cache.put(4, 40)
print(cache.get(1))  # -1
print(cache.get(3))  # 30
print(cache.get(4))  # 40