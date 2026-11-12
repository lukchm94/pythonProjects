"""Interview exercise: Detect conflicting idempotency-key reuse.

Target time: 30-45 minutes.

Implement ``IdempotencyExecutor.execute(key, payload, operation)`` for
synchronous operations with string payloads.

Requirements:
- The first call for a non-empty string key runs ``operation(payload)`` and
  stores the payload and successful result.
- A later call with the same key and payload returns the stored result without
  running its operation.
- Reusing a key with a different payload raises ``IdempotencyConflictError``
  and does not run the operation.
- If an operation raises, do not store a result; a later call may retry it.
- Reject empty or non-string keys with ``ValueError``.

This exercise is single-threaded and in-memory. Add focused tests for replay,
payload conflicts, failure and retry, and invalid keys.
"""

from collections.abc import Callable
from typing import TypeVar

R = TypeVar("R")


class IdempotencyConflictError(ValueError):
    """Raised when a key is reused with a different payload."""


class IdempotencyExecutor:
    def execute(
        self, key: str, payload: str, operation: Callable[[str], R]
    ) -> R:
        # TODO: Replay matching requests and reject conflicting payloads.
        raise NotImplementedError
