FROM python:3.9-alpine

RUN apk --no-cache add python3-dev py3-pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "app.py"]