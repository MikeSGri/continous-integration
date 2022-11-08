FROM python:3.10.6

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --user -r requirements.txt
COPY . .

WORKDIR /usr/src/app/finance


CMD python manage.py runserver 0.0.0.0:8000