default: clean install

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name '*.egg-info' -delete

install:
	pip install -r requirements.txt
	pip install -e .[test]

image:
	docker build -t cryptopians-notifier .

flake8:
	flake8 --exclude=tests src

isort:
	isort --recursive --check-only --diff src/cn

lint: flake8 isort
