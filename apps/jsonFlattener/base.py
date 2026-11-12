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


def handle_dict(value: dict[str, Any]) -> dict[str, Any]:
    flat_dict: dict[str, Any] = {}
    for key in value.keys():
        v = value[key]

        if type(v) is not list:
            if type(v) is str:
                flat_dict[key] = v
            else:
                flat_dict[key] = ""

        val_len = len(v)

        for index in range(val_len):
            if type(v[index]) is dict:
                for flat_key in v[index].keys():
                    index_name: str = f"{key}.{index}.{flat_key}"

                    flat_dict[index_name] = v[index][flat_key]

                flat_dict

    return flat_dict


def flatten(value: dict[str, Any] | list[Any]) -> dict[str, Any]:
    """Convert a nested dictionary/list into a dot-path mapping."""

    if type(value) is dict:
        return handle_dict(value)

    elif type(value) is list:
        flat_dict: dict[str, Any] = {}
        for index in range(len(value)):
            if type(value[index]) is dict:
                flat_dict.update(handle_dict(value[index]))
            else:
                key = f"{index}"
                flat_dict[key] = ""

        return flat_dict

    else:
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
