# Python Projects

This repository contains independent Python applications. Each app uses PDM,
supports Python 3.12 or newer, and keeps its own dependencies, lockfile, and
virtual environment.

The workspace recommends the Ruff VS Code extension. Python files are
formatted on save, with Ruff lint fixes and import sorting applied on save.
The repository-wide Ruff rules are configured in `.ruff.toml`.

## QR code generator

```sh
cd apps/qrCodeGenerator
pdm sync
pdm run python weddingQr.py
```

To generate a Wi-Fi QR code instead:

```sh
pdm run python qrFactory.py
```

## Name decorator

```sh
cd apps/nameDecorator
pdm sync
pdm run name-decorator
```

## Practice problems

Each problem is an independent PDM app. Its `main.py` contains the exercise
description and starter interfaces; complete the TODOs to solve it.

| Problem | App |
| --- | --- |
| 1. LRU cache with TTL and metrics | `apps/cache` |
| 2. Nested JSON/dict flattener and unflattener | `apps/jsonFlattener` |
| 3. Thread-safe token bucket rate limiter | `apps/rateLimiter` |
| 4. Async batcher with bounded backpressure | `apps/asyncBatcher` |
| 5. Retry and circuit-breaker decorator | `apps/retryCircuitBreaker` |
| 6. Type-safe configuration loader | `apps/typedConfig` |
| 7. Object pooling and memory optimization | `apps/objectPool` |

For example:

```sh
cd apps/jsonFlattener
pdm sync
pdm run json-flattener
```
