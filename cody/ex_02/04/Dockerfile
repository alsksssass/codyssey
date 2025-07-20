FROM alpine:latest

WORKDIR /app

RUN apk add --no-cache python3 py3-pip
COPY . .

RUN python3 -m venv venv
RUN . venv/bin/activate && pip install -r requirements.txt

EXPOSE 80

CMD ["venv/bin/python", "-m", "gunicorn", "app:app", "--bind", "0.0.0.0:80"]


