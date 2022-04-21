from prometheus_client import start_http_server
from src.metrics_handler import init, update_all
from src.util import api
import time


if __name__ == '__main__':
    cfg = {
        "ns2_stats_api_url": "http://host.docker.internal:8080/stats",

        "server_port": 9091,
        "metrics_update_interval_in_seconds": 3600
    }
    api_data = api.get_ns2_api_data(cfg["ns2_stats_api_url"])
    init()

    # Start up the server to expose the metrics_handler.
    server_port = cfg["server_port"]
    start_http_server(server_port)
    print("Starting server on port %s...\nhttp://localhost:%s/" % (str(server_port), str(server_port)))

    # Generate some requests.
    while True:
        update_all(api_data)
        time.sleep(cfg["metrics_update_interval_in_seconds"])
