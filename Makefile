default: clean install

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name '*.egg-info' -delete

install:
	pip install -r requirements.txt
	pip install -e .

image:
	docker build -t cryptopians-notififer .
