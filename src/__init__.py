from prometheus_client import start_http_server
from metrics import init_metrics, update_metrics
from util import api, config
import time


if __name__ == '__main__':
    cfg = config.get()
    print(api.get_ns2_api_data(cfg["ns2_stats_api_url"]))
    # init_metrics()

    print(config.get())

    # Start up the server to expose the metrics.
    start_http_server(8000)
    print("Starting server on port 8000...\nhttp://localhost:8000/metrics")

    # Generate some requests.
    while True:
        # update_metrics()
        time.sleep(1)
