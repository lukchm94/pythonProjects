"""Beginner exercise: Ignore duplicate events and retry failures.

Target time: 20-30 minutes.

Implement ``process_event_once`` for a single-threaded, in-memory event
handler.

Requirements:
- If ``event_id`` is already in ``processed_ids``, return False without
  running ``action``.
- Otherwise, run ``action``. After it succeeds, add ``event_id`` to
  ``processed_ids`` and return True.
- If ``action`` raises, propagate the exception and do not mark the event as
  processed, so a later call can retry it.

Use the standard library only. Add focused tests for duplicate suppression,
successful processing, and failure followed by retry. This exercise does not
provide persistence, concurrency, or exactly-once guarantees for external
side effects.
"""

from collections.abc import Callable


def process_event_once(
    event_id: str,
    processed_ids: set[str],
    action: Callable[[], None],
) -> bool:
    # TODO: Skip completed event IDs and mark new ones only after success.
    raise NotImplementedError
