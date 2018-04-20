from os import environ

CN_BOT_NAME = environ.get('CN_BOT_NAME', 'Cryptopians Notifier')
CN_INTERVAL = environ.get('CN_INTERVAL', 60)
CN_EXCHANGES = environ.get('CN_EXCHANGES', 'binance,bittrex')
CN_DEBUG_ENDPOINT = environ.get('CN_DEBUG_ENDPOINT', '')

S3_BUCKET_NAME = environ.get('S3_BUCKET_NAME', '')
S3_FILE_NAME = environ.get('S3_FILE_NAME', 'cryptopians_notifier.json')

SLACK_WEBHOOK_URL = environ.get('SLACK_WEBHOOK_URL', '')
