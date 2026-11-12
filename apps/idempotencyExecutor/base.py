"""Interview exercise: Replay successful results for duplicate requests.

Target time: 30-45 minutes.

Implement ``IdempotencyExecutor.execute(key, operation)`` as an in-memory
helper for synchronous operations.

Requirements:
- The first call for a non-empty string key runs ``operation`` and stores its
  successful result.
- Later calls with the same key return the stored result without running
  their operation.
- If an operation raises, do not store a result; a later call may retry it.
- Reject empty or non-string keys with ``ValueError``.

This exercise is single-threaded and does not provide persistence or atomicity
for external side effects. Add focused tests for replay, failure and retry,
and invalid keys.
"""

from collections.abc import Callable
from typing import TypeVar

R = TypeVar("R")


class IdempotencyExecutor:
    def execute(self, key: str, operation: Callable[[], R]) -> R:
        # TODO: Cache successful results by key and replay them on duplicates.
        raise NotImplementedError
