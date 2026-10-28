# ## Problem 1: LRU Cache with TTL (Time-To-Live) & Metrics
# The Problem Description
# Implement a thread-safe LRUCache class that handles time-to-live (TTL) expiration and collects usage metrics.

# Your cache must support the following methods:

# __init__(self, capacity: int): Initializes the cache with a maximum capacity.

# get(key): Returns the value of the key if the key exists and has not expired. Otherwise, returns None. Accessing an item updates its most-recently-used status.

# put(key, value, ttl: float | None = None): Inserts or updates the value. If the cache exceeds capacity (or contains expired items), it must evict the least recently used item. If a ttl (in seconds) is provided, the item should expire after that duration.

# get_metrics() -> dict: Returns a dictionary tracking performance metrics, such as:

# Hit rate (hits / total lookups)

# Miss rate (misses / total lookups)

# Total evictions (capacity-based + TTL-based)