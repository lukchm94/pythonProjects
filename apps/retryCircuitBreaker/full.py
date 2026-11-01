"""Full exercise: Problem 5: Implement a retry and circuit-breaker decorator.

Create ``retry_with_circuit_breaker`` as a decorator factory for synchronous
and asynchronous functions.

Requirements:
- Retry configured exception types up to ``max_retries`` additional attempts,
  optionally waiting ``retry_delay`` seconds between attempts.
- Count consecutive failures across calls. Open the circuit after
  ``failure_threshold`` failures and reject calls with ``CircuitOpenError``.
- After ``recovery_timeout``, allow one call through as a trial. Close the
  circuit on success; reopen it on failure.
- Keep state per decorated function, and synchronize state updates so
  simultaneous calls cannot corrupt the circuit state.
- Preserve the wrapped function's metadata and do not swallow cancellation
  or exceptions outside the configured retry set.

Provide equivalent behavior for sync and async functions. Use an injectable
clock/sleep strategy if useful for deterministic tests.
"""

from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


class CircuitOpenError(RuntimeError):
    """Raised when a call is rejected by an open circuit."""


def retry_with_circuit_breaker(
    *,
    max_retries: int,
    failure_threshold: int,
    recovery_timeout: float,
    retry_delay: float = 0,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[F], F]:
    # TODO: Return a decorator that wraps sync and async callables safely.
    raise NotImplementedError
