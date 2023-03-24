FROM python:3.10-slim-buster

ENV TZ=America/Los_Angeles
ENV PYTHONUNBUFFERED=1

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN mkdir /app/src

COPY src/ /app/src/

RUN mkdir /app/config
RUN mkdir /app/logs 

COPY config/config.example.yml /app/config/config.yml 
RUN touch /app/logs/container-updater.logs

CMD ["python", "-u", "src/main.py"]