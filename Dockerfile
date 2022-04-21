FROM python

WORKDIR /code

ENV ns2_stats_api_url="http://host.docker.internal:8080/stats",
ENV server_port: 9091,
ENV metrics_update_interval_in_seconds: 3600

EXPOSE 8080
EXPOSE 9091

COPY . /code

RUN python -m venv venv

RUN pip install -r requirements.txt

CMD python -m src
