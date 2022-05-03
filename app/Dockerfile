FROM python:buster

COPY server /server
COPY trello_app /trello_app
COPY .env /.

RUN pip3 install -r server/requirements.txt

EXPOSE 8000/tcp

CMD ["python3", "server/main.py"]
