"""Interview exercise: Implement a simple bounded object pool.

Target time: 30-45 minutes.

Implement a pool for ``PooledItem`` instances.

Requirements:
- ``acquire()`` returns an idle item when available, otherwise creates one.
- ``release(item)`` resets the item's value and returns it to the pool.
- Keep no more than ``max_size`` idle items; discard excess released items.
- Reject a non-positive ``max_size``.

This version is single-threaded and assumes callers release only items
acquired from this pool, at most once. Ownership checks, double-release
detection, metrics, weak references, and thread safety are follow-ups.
"""

from dataclasses import dataclass


@dataclass
class PooledItem:
    value: str = ""

    def reset(self) -> None:
        self.value = ""


class ObjectPool:
    def __init__(self, max_size: int) -> None:
        # TODO: Validate max_size and initialize idle storage.
        raise NotImplementedError

    def acquire(self) -> PooledItem:
        # TODO: Reuse an idle item or create a new one.
        raise NotImplementedError

    def release(self, item: PooledItem) -> None:
        # TODO: Reset the item and store it if the pool has room.
        raise NotImplementedError
