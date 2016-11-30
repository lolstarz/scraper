FROM tiangolo/uwsgi-nginx-flask:flask-python3.5

RUN python -m pip install lxml
RUN python -m pip install requests
RUN python -m pip install beautifulsoup4

COPY ./app /app
