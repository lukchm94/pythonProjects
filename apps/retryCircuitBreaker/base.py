"""Interview exercise: Add retry behavior to a synchronous function.

Target time: 30-45 minutes.

Implement ``retry`` as a decorator factory.

Requirements:
- Accept ``max_retries`` as the number of additional attempts after the first.
- Retry only the configured exception types.
- Propagate the final exception when attempts are exhausted.
- Do not retry exceptions outside the configured exception types.
- Preserve the wrapped function's metadata.

Keep this version synchronous and without delays. Circuit breaking, async
support, and concurrent state coordination are follow-ups.
"""

from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def retry(
    *,
    max_retries: int,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[F], F]:
    # TODO: Return a decorator that retries matching failures.
    raise NotImplementedError
