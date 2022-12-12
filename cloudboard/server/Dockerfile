FROM python:3.9

COPY . /root/app
WORKDIR /root/app

RUN apt-get install python3-pip
RUN pip install flask flask-login flask-sqlalchemy jsonpickle pyjwt

CMD ["export", "FLASK_APP=/root/app"]
CMD ["export", "FLASK_DEBUG=1"]

CMD ["flask", "run"]