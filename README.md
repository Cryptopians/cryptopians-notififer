# Cryptopians Notifier

## Requirements

* Python 3.6
* Docker

## Installation

Install requirements

```
pip install -r requirements.txt
```

Install (cryptopians-notififer, a.k.a. cn):

```
pip install -e .
```

Or run these steps with at once with `make`.

## Usage

Run the script with `cn` or use docker `docker-compose up`.

## Environment variables

The following environment variables can be used:

```python
CN_BOT_NAME # Cryptopians Notifier
CN_INTERVAL # 10 (seconds)
CN_EXCHANGES # ['bittrex']
```

## Todos

* Make it scalable. Currently trading pairs per exchange are kept in memory. We
prefer this to be stored in a (any kind of) database or persistant storage.
* Add top 10 exchanges
