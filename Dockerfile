FROM python:3
ENV PYTHONUNBUFFERED 1
# Prevent the writing of .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# Collect static media
RUN python /code/manage.py collectstatic --noinput
