"""Interview exercise: Fetch a finite batch with bounded concurrency.

Target time: 30-45 minutes.

Implement ``fetch_all`` for a finite collection of inputs and an injected
async fetch function.

Requirements:
- Run at most ``max_concurrency`` fetch calls at once.
- Return results in the same order as the input items.
- Validate that ``max_concurrency`` is positive.
- Do not use a real network or third-party HTTP package; tests can inject a
  fake async fetch function.

Use ``asyncio.gather`` with a semaphore or another straightforward approach.
Retries, bounded producer backpressure, and cancellation edge cases are
follow-ups.
"""

from collections.abc import Awaitable, Callable, Iterable
from typing import TypeVar

T = TypeVar("T")
R = TypeVar("R")


async def fetch_all(
    items: Iterable[T],
    fetch: Callable[[T], Awaitable[R]],
    *,
    max_concurrency: int,
) -> list[R]:
    # TODO: Limit concurrent fetches and preserve input order in the results.
    raise NotImplementedError
