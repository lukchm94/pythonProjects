# Python Projects

This repository contains independent Python applications. Each app uses PDM,
supports Python 3.12 or newer, and keeps its own dependencies, lockfile, and
virtual environment.

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
