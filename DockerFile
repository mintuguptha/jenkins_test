FROM python:3.8-slim-buster
WORKDIR /app
RUN pip install flask
COPY application.py ./application.py
CMD ["flask","--app","application","run","--host=0.0.0.0"]
