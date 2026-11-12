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


if __name__ == "__main__":
    cases: list[tuple[str, dict[str, Any] | list[Any], dict[str, Any]]] = [
        (
            "nested example",
            {"users": [{"name": "Ada"}]},
            {"users.0.name": "Ada"},
        ),
        (
            "mixed containers",
            {"a": [1, {"b": [True, None]}]},
            {"a.0": 1, "a.1.b.0": True, "a.1.b.1": None},
        ),
        ("empty root dict", {}, {"": {}}),
        ("empty root list", [], {"": []}),
        ("empty nested containers", {"a": [], "b": {}}, {"a": [], "b": {}}),
        (
            "scalar dict values",
            {"n": 3, "flag": False, "none": None},
            {"n": 3, "flag": False, "none": None},
        ),
    ]

    for name, value, expected in cases:
        try:
            actual = flatten(value)
        except Exception as error:
            print(f"{name}: raised {type(error).__name__}: {error}")
            continue

        print(f"{name}:")
        print(f"  expected: {expected!r}")
        print(f"  actual:   {actual!r}")
