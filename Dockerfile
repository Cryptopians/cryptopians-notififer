FROM python:3.6 AS builder
RUN apt-get update
RUN mkdir -p /opt/dist
WORKDIR /code
COPY requirements.txt /code
COPY . /code
RUN python setup.py bdist_wheel && mv dist/*.whl /opt/dist/

FROM python:3.6
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt --no-cache-dir
COPY --from=builder /opt/dist /opt/dist
RUN pip install /opt/dist/*.whl
CMD ["cn"]
