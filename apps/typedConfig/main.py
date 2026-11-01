"""Problem 6: Build a type-safe configuration loader.

Implement ``Config.from_env(prefix)`` using class annotations as the schema.
Subclasses declare fields and may provide defaults as class attributes:

    class AppConfig(Config):
        host: str
        port: int = 8000
        debug: bool = False


Environment variables are named ``{prefix}_{FIELD}`` (uppercase field name).
Support ``str``, ``int``, ``float``, and ``bool``; accept true/false, 1/0,
yes/no, and on/off for booleans, case-insensitively.

Requirements:
- Missing required values and invalid values produce clear exceptions that
  name the field and source environment variable.
- Convert values to the declared type and expose them as instance attributes.
- Validate subclass declarations when the class is created, using either
  ``__init_subclass__`` or a metaclass.
- Do not read environment variables until ``from_env`` is called.
"""

from typing import Self


class Config:
    @classmethod
    def from_env(cls, prefix: str) -> Self:
        # TODO: Read annotated fields, parse values, and construct the subclass.
        raise NotImplementedError


class AppConfig(Config):
    host: str
    port: int = 8000
    debug: bool = False
