"""Beginner exercise: Make state updates idempotent.

Target time: 15-20 minutes.

Implement ``set_subscription`` to add or remove a user from a subscription
set.

Requirements:
- When ``subscribed`` is True, ensure ``user_id`` is in ``subscribers``.
- When ``subscribed`` is False, ensure ``user_id`` is not in ``subscribers``.
- Repeating the same update must not change the result.
- Do not toggle membership; preserve all other subscribers.

Use the standard library only. Add focused tests for repeated subscribe and
unsubscribe requests and for preserving unrelated users.
"""


def set_subscription(
    subscribers: set[str], user_id: str, subscribed: bool
) -> None:
    # TODO: Set the requested membership state without toggling it.
    raise NotImplementedError
