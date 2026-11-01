"""Problem 1: Implement a thread-safe LRU cache with TTL and metrics.

Requirements:
- ``LRUCache(capacity)`` stores at most ``capacity`` key/value pairs.
- ``get(key)`` returns the value or None. A successful lookup makes the key
  most recently used; a missing or expired key is a miss.
- ``put(key, value, ttl=None)`` inserts or replaces a key. A TTL is in seconds;
  expired entries should be removed and counted as evictions. ``get`` removes
  an expired requested key; ``put`` may purge expired entries before evicting
  for capacity.
- When capacity is exceeded, evict the least recently used entry and count it.
- ``get_metrics()`` returns hits, misses, hit_rate, miss_rate, and evictions.
  A cache with no lookups has hit_rate and miss_rate equal to 0.
- All public operations must be safe to call from multiple threads.

Use a monotonic clock for expiry. Decide how to handle invalid capacities and
non-positive TTLs, and document your choice.
"""

from typing import Any


class LRUCache:
    def __init__(self, capacity: int) -> None:
        # TODO: Initialize storage, synchronization, and metric counters.
        raise NotImplementedError

    def get(self, key: Any) -> Any | None:
        # TODO: Expire stale entries, update recency, and record a hit or miss.
        raise NotImplementedError

    def put(self, key: Any, value: Any, ttl: float | None = None) -> None:
        # TODO: Insert or update the value and evict entries when necessary.
        raise NotImplementedError

    def get_metrics(self) -> dict[str, int | float]:
        # TODO: Return a snapshot of the requested metrics.
        raise NotImplementedError
