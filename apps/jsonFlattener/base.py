"""Interview exercise: Flatten nested dictionaries and lists.

Target time: 30-45 minutes.

Implement ``flatten`` using dot-separated paths. List indices are decimal
path segments, so ``{"users": [{"name": "Ada"}]}`` becomes
``{"users.0.name": "Ada"}``.

Requirements:
- Support nested dictionaries and lists, preserving scalar values and types.
- Preserve empty dictionaries and lists.
- Represent an empty root dictionary or list with the empty path ``""``.
- Dictionary keys are non-empty strings and may not contain dots or consist
  only of decimal digits.

Implement only ``flatten`` for this interview exercise. Add focused tests for
nested mixed containers, scalar values, and empty containers. Unflattening,
malformed-path handling, and arbitrary-depth robustness are follow-ups.
"""

from typing import Any


def flatten(value: dict[str, Any] | list[Any]) -> dict[str, Any]:
    """Convert a nested dictionary/list into a dot-path mapping."""
    # TODO: Walk nested containers and emit scalar and empty-container leaves.
    raise NotImplementedError
