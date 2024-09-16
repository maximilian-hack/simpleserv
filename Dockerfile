FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

COPY server.py /usr/src/app/server.py

EXPOSE 8080

CMD ["python", "server.py"]
