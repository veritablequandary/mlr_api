FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN pip install --no-cache -r requirements.txt

CMD ["/bin/sh", "/app/start.sh"]