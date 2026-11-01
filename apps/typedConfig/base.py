"""Interview exercise: Load basic typed settings from environment variables.

Target time: 30-45 minutes.

Implement ``Config.from_env(prefix)`` using annotations as the schema.
Subclasses declare fields and may provide defaults as class attributes:

    class AppConfig(Config):
        host: str
        port: int = 8000
        debug: bool = False

Read variables named ``{prefix}_{FIELD}``, with the field name uppercased.
Support ``str``, ``int``, ``float``, and ``bool``; for booleans accept
``true``/``false`` and ``1``/``0`` case-insensitively.

Requirements:
- Missing required settings and invalid values raise clear ``ValueError``
  messages naming the field and environment variable.
- Convert values to their annotated types and expose them as instance attrs.
- Do not read the environment until ``from_env`` is called.

Subclass-definition validation and additional boolean spellings are
follow-ups.
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
