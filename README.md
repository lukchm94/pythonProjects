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

Each problem is an independent PDM app. Its `base.py` is a focused interview
exercise; where present, `full.py` contains the extended take-home version.
Complete the base exercises in the suggested order below, then try any
corresponding full versions as extensions.

| Order | Interview exercise | Base file |
| --- | --- | --- |
| 1 | LRU cache | `apps/cache/base.py` |
| 2 | Flatten nested JSON-compatible data | `apps/jsonFlattener/base.py` |
| 3 | Load typed settings from environment variables | `apps/typedConfig/base.py` |
| 4 | Add retry behavior to a synchronous function | `apps/retryCircuitBreaker/base.py` |
| 5 | Implement a token bucket rate limiter | `apps/rateLimiter/base.py` |
| 6 | Build a bounded object pool | `apps/objectPool/base.py` |
| 7 | Fetch a batch with bounded async concurrency | `apps/asyncBatcher/base.py` |
| 8 | Replay successful results for duplicate idempotency keys | `apps/idempotencyExecutor/base.py` |
| 9 | Reject idempotency keys reused with a different payload | `apps/idempotencyPayload/base.py` |
| 10 | Coordinate concurrent requests with the same idempotency key | `apps/idempotencyConcurrency/base.py` |

For example:

```sh
cd apps/jsonFlattener
pdm sync
pdm run json-flattener
```
