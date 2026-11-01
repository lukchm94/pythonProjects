"""Interview exercise: Implement a token bucket rate limiter.

Target time: 30-45 minutes.

Implement ``TokenBucket`` with a positive capacity and refill rate in tokens
per second.

Requirements:
- Start with a full bucket.
- ``allow_request(cost=1)`` consumes the cost and returns True when enough
  tokens are available; otherwise return False without consuming tokens.
- Refill continuously based on elapsed time, capped at capacity.
- Reject non-positive capacity, refill rates, and request costs, and reject
  costs greater than capacity.
- Use ``time.monotonic()`` to measure elapsed time.
- ``available_tokens()`` returns the current refilled token count.

Implement this as a single-threaded exercise. Clock injection and thread
safety are follow-ups.
"""

class TokenBucket:
    def __init__(self, capacity: float, refill_rate: float) -> None:
        # TODO: Validate configuration and initialize full bucket state.
        raise NotImplementedError

    def allow_request(self, cost: float = 1) -> bool:
        # TODO: Refill, validate the cost, and consume tokens if available.
        raise NotImplementedError

    def available_tokens(self) -> float:
        # TODO: Refill and report the current token count.
        raise NotImplementedError
