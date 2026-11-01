"""Problem 3: Implement a thread-safe token bucket rate limiter.

The bucket has a positive token capacity and positive refill rate in tokens
per second. ``allow_request(cost=1)`` should atomically consume ``cost`` tokens
and return whether the request was allowed.

Requirements:
- Refill continuously based on elapsed time, capped at bucket capacity.
- Raise ``ValueError`` for invalid configuration or costs that are non-positive
  or larger than the capacity.
- Make concurrent calls safe; no request may consume tokens that another
  concurrent call has already consumed.
- Use a monotonic clock. Allow a clock to be injected so tests can advance
  time without sleeping.
- Include a method to report the currently available token count.

Implement the token bucket first. Comparing it with a leaky bucket is an
optional extension.
"""

from collections.abc import Callable


class TokenBucket:
    def __init__(
        self,
        capacity: float,
        refill_rate: float,
        clock: Callable[[], float] | None = None,
    ) -> None:
        # TODO: Validate configuration and initialize synchronized state.
        raise NotImplementedError

    def allow_request(self, cost: float = 1) -> bool:
        # TODO: Refill and consume tokens atomically.
        raise NotImplementedError

    def available_tokens(self) -> float:
        # TODO: Refill and return the current token count.
        raise NotImplementedError
