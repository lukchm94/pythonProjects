"""Interview exercise: Handle concurrent duplicate requests safely.

Target time: 45-60 minutes.

Implement ``ConcurrentIdempotencyExecutor.execute(key, payload, operation)``
for synchronous operations with string payloads.

Requirements:
- The first call for a non-empty string key runs ``operation(payload)`` and
  stores its successful result.
- Concurrent calls with the same key and payload wait for that operation and
  receive its successful result without running their own operation.
- Reusing a key with a different payload raises ``IdempotencyConflictError``,
  including while the first operation is still running.
- If an operation raises, calls already waiting for it receive its failure;
  remove the failed entry so a later call can retry.
- Different keys must be able to run their operations concurrently.
- Reject empty or non-string keys with ``ValueError``.

Use only the standard library. Add deterministic tests for duplicate calls,
payload conflicts, failure and retry, and parallel calls with different keys.
Do not use arbitrary sleeps in concurrency tests.
"""

from collections.abc import Callable
from typing import TypeVar

R = TypeVar("R")


class IdempotencyConflictError(ValueError):
    """Raised when a key is reused with a different payload."""


class ConcurrentIdempotencyExecutor:
    def execute(
        self, key: str, payload: str, operation: Callable[[str], R]
    ) -> R:
        # TODO: Coordinate in-flight operations and replay successful results.
        raise NotImplementedError
