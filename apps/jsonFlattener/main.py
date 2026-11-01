"""Problem 2: Flatten and rebuild nested JSON-compatible data.

Implement ``flatten`` and ``unflatten`` for dictionaries and lists. Use dot
notation for paths and decimal list indices (for example,
``{"users": [{"name": "Ada"}]}`` becomes ``{"users.0.name": "Ada"}``).

Requirements:
- Preserve scalar values and their Python types; do not stringify values.
- Preserve empty dictionaries and lists.
- Dictionary keys must be non-empty strings and may not contain dots or
  consist only of decimal digits. This keeps dictionary keys distinct from
  list indices.
- Represent an empty root dictionary or list with the single empty path ``""``.
- Reject malformed paths and conflicting paths instead of silently
  overwriting data.
- Do not impose an arbitrary application-level nesting-depth limit.

Complete the functions below. Choose recursion or iteration and add tests for
empty containers, mixed lists/dictionaries, and invalid input.
"""

from typing import Any


def flatten(value: dict[str, Any] | list[Any]) -> dict[str, Any]:
    """Convert a nested dictionary/list into a dot-path mapping."""
    # TODO: Walk nested containers and emit scalar and empty-container leaves.
    raise NotImplementedError


def unflatten(paths: dict[str, Any]) -> dict[str, Any] | list[Any]:
    """Rebuild nested dictionaries/lists from a dot-path mapping."""
    # TODO: Validate paths and reconstruct the original container structure.
    raise NotImplementedError
