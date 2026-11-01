"""Full exercise: Problem 7: Implement an object pool and optimize its pooled objects.

Create a bounded, thread-safe pool for instances of ``PooledItem``.

Requirements:
- ``acquire()`` returns a reusable item or creates one with a factory.
- ``release(item)`` resets and returns an acquired item to the pool. Reject
  items that are foreign to the pool or already released.
- Keep at most ``max_size`` idle items; discard excess released items.
- Track how many objects were created, reused, and discarded.
- Use ``__slots__`` on ``PooledItem`` and make instances weak-referenceable.
- Avoid keeping unnecessary strong references to discarded items.

Consider how your pool detects ownership and double release without creating
an unbounded registry. Add tests for concurrent use, reuse, and capacity.
"""

from dataclasses import dataclass


@dataclass(slots=True, weakref_slot=True)
class PooledItem:
    value: str = ""


class ObjectPool:
    def __init__(self, max_size: int) -> None:
        # TODO: Initialize a synchronized bounded pool and its counters.
        raise NotImplementedError

    def acquire(self) -> PooledItem:
        # TODO: Reuse an idle item or create a new one.
        raise NotImplementedError

    def release(self, item: PooledItem) -> None:
        # TODO: Validate ownership/state, reset, and return or discard the item.
        raise NotImplementedError

    def get_metrics(self) -> dict[str, int]:
        # TODO: Return created, reused, and discarded counts.
        raise NotImplementedError
