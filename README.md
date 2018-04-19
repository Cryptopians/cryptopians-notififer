# Cryptopians Notifier

## Requirements

* Python 3.6
* Docker

## Installation

Install requirements

```
pip install -r requirements.txt
```

Install (cryptopians-notifier, a.k.a. cn):

```
pip install -e .
```

Or run these steps at once with `make`.

## Usage

Run the script with `cn` or use docker `docker-compose up`.

## Environment variables

The following environment variables can be used:

```python
CN_BOT_NAME  # Cryptopians Notifier
CN_INTERVAL  # 60 (seconds)
CN_EXCHANGES  # ['binance', 'bittrex']
S3_BUCKET_NAME  # The name of the S3 bucket to use
S3_FILE_NAME  # cryptopians_notifier.json
SLACK_WEBHOOK_URL  # https://hooks.slack.com/services/xxx/yyy/zzz
```

This library uses AWS S3 to store its data, therefor the following credentials
are required (`boto3`):

```python
AWS_DEFAULT_REGION  # The default region to use, e.g. eu-west-1, etc.
AWS_ACCESS_KEY_ID  # The access key for your AWS account
AWS_SECRET_ACCESS_KEY  # The secret key for your AWS account.
```

## Todos

* Make it scalable. Currently trading pairs per exchange are kept in memory. We
prefer this to be stored in a (any kind of) database or persistant storage.
* Add top 60 exchanges.
