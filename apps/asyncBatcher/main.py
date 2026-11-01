"""Problem 4: Build an async scraper/API batcher with bounded backpressure.

Implement ``fetch_all`` as the concurrent worker core of a scraper or API
client. Process an iterable of inputs using an injected async fetch function
and return results in the same order as the inputs.

Requirements:
- Never run more than ``max_concurrency`` fetches at once.
- Bound queued work to ``max_pending`` items; do not create one task per input.
- Retry a failed fetch up to ``retries`` additional times, then propagate its
  final exception.
- Do not swallow cancellation. Validate positive limits and non-negative
  retry counts.
- Do not require a real network or third-party HTTP package; tests can inject
  a fake fetch function.

Use an ``asyncio.Queue`` or another approach that applies backpressure to the
producer. Add tests for ordering, concurrency limits, retries, and cancellation.
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
    max_pending: int,
    retries: int = 0,
) -> list[R]:
    # TODO: Implement a bounded producer/worker pipeline.
    raise NotImplementedError
