FROM python:3.9.4-slim

WORKDIR /

COPY ./main.py /main.py
COPY ./requirements.txt /requirements.txt

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        python3-dev \
        python3-setuptools \
        libmariadb-dev \
        make \
        gcc \
        curl

RUN python3 -m pip install -r requirements.txt --no-deps

RUN apt-get remove -y --purge make gcc build-essential curl && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN echo $TZ > /etc/timezone

CMD [ "python", "main.py" ]