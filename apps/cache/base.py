"""Interview exercise: Implement a basic LRU cache.

Target time: 30-45 minutes.

Implement ``LRUCache`` with a positive capacity and the following behavior:
- ``get(key)`` returns the stored value, or None when the key is missing.
- A successful ``get`` makes the key most recently used.
- ``put(key, value)`` inserts or replaces a value.
- If inserting a new key at capacity, evict the least recently used key.
- Replacing an existing key must not evict another entry.

Use the standard library only. Add focused tests for lookup, replacement,
recency, and capacity. TTL, metrics, and thread safety are follow-up tasks.
"""

from typing import Any


class LRUCache:
    def __init__(self, capacity: int) -> None:
        # TODO: Validate capacity and initialize storage.
        raise NotImplementedError

    def get(self, key: str) -> Any | None:
        # TODO: Return the value and mark the key as most recently used.
        raise NotImplementedError

    def put(self, key: str, value: Any) -> None:
        # TODO: Insert or replace the value, evicting the LRU key if needed.
        raise NotImplementedError
