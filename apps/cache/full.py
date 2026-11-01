"""Full exercise: Build a thread-safe LRU cache with TTL and metrics.

This is the extended, take-home version. The current implementation below is
the working attempt carried over from ``main.py``; it does not yet satisfy all
requirements.

Requirements:
- ``LRUCache(capacity)`` stores at most ``capacity`` key/value pairs.
- ``get(key)`` returns the value or None. A successful lookup makes the key
  most recently used; a missing or expired key is a miss.
- ``put(key, value, ttl=None)`` inserts or replaces a key. TTLs are in
  milliseconds; the constructor TTL is the default. Reject non-positive
  capacity and TTL values.
- Use a monotonic clock for expiry. ``get`` removes an expired requested key;
  ``put`` may purge expired entries before making room.
- When capacity is reached, evict the least recently used entry. Count both
  expired-entry removals and capacity evictions as evictions.
- ``get_metrics()`` returns hits, misses, hit_rate, miss_rate, and evictions.
  With no lookups, both rates are 0.
- All public operations must be safe to call from multiple threads.

Add tests for TTL boundaries, replacement, recency, capacity, metrics, and
concurrent access. Background cleanup is not required.
"""

from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Any


class ErrorNames(Enum):
    CAPACITY = "capacity"
    TTL = "ttl"


class ValueError(Exception):
    base_msg: str = "Provided {value} must be > 0. Received: "

    def __init__(self, name: str, amt: int) -> None:
        msg = self.base_msg.format(value=name)
        self.message = f"{msg}{str(amt)}"
        super(self.message)


class CapacityError(ValueError):
    def __init__(self, amt: int, name: str = ErrorNames.CAPACITY.value) -> None:
        super(name, amt)


class TtlError(ValueError):
    def __init__(self, amt: int, name: str = ErrorNames.TTL.value) -> None:
        super(name, amt)


class ExceededCacheCapacityError(Exception):
    base_msg: str = "Exceeded allowed cache capacity of: {cap}, actual: {act}"

    def __init__(self, cap: int, act: int) -> None:
        message = self.base_msg.format(cap=cap, act=act)
        self.message = message
        super(self.message)


class CacheItem:
    value: Any
    expired_at: datetime

    def __init__(self, value: Any, expired_at: datetime):
        self.value = value
        self.expired_at = expired_at


class LRUCache:
    capacity: int
    cache: dict[str, CacheItem]
    ttl: int  # TTL in milliseconds
    tz: timezone

    def __init__(self, capacity: int = 10, ttl: int = 18000) -> None:
        self.tz = timezone.utc
        self.cache = {}

        if capacity <= 0:
            raise CapacityError(capacity)
        self.capacity = capacity

        if ttl <= 0:
            raise TtlError(ttl)
        self.ttl = ttl

    def get(self, key: str) -> Any | None:
        item: CacheItem | None = self.cache.get(key)

        if item is None:
            return item

        if self.__is_expired(item):
            self.cache.pop(key)
            return None

        return item.value

    def put(self, key: str, value: Any, ttl: int | None = None) -> None:
        return (
            self.__handle_cache_cap(key, value, ttl)
            if self.__exceeds_capacity(key)
            else self.__insert_item(key, value, ttl)
        )

    def get_metrics(self) -> dict[str, int | float]:
        # TODO: Return a snapshot of the requested metrics.
        raise NotImplementedError

    def __is_expired(self, item: CacheItem) -> bool:
        now = self.__now()

        return True if item.expired_at <= now else False

    def __now(self) -> datetime:
        return datetime.now(self.tz)

    def __exceeds_capacity(self, key: str) -> bool:
        current_exists = self.cache.get(key)
        if current_exists is not None:
            return False

        return len(self.cache) >= self.capacity

    def __validate_ttl(self, ttl: Any) -> int:
        if ttl is None or type(ttl) is not int:
            raise TtlError(ttl)

        if ttl <= 0:
            raise TtlError(ttl)

        return int(ttl)

    def __cache_cleared(self) -> bool:
        for key in self.cache.keys():
            self.__evaluate_cache_item_expiration(key)

            if len(self.cache) < self.capacity:
                return True

        return False

    def __evaluate_cache_item_expiration(self, key: str) -> None:
        item = self.cache.get(key)

        if item is None:
            return

        if self.__is_expired(item):
            self.cache.pop(key)

    def __handle_cache_cap(self, key: str, value: Any, ttl: int | None = None) -> None:
        if self.__cache_cleared():
            return self.__insert_item(key, value, ttl)

        raise ExceededCacheCapacityError(self.capacity, len(self.cache))

    def __insert_item(self, key: str, value: Any, ttl: int | None = None) -> None:
        now = self.__now()
        valid_ttl: int = self.ttl if ttl is None else self.__validate_ttl(ttl)
        expired_at: datetime = now + timedelta(milliseconds=valid_ttl)
        item: CacheItem = CacheItem(value, expired_at)

        self.cache[key] = item
