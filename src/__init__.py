__all__ = (
    'metrics',
    'util'
)

from prometheus_client import start_http_server
from src.metrics import init, update_all
from util import api, config
import time


if __name__ == '__main__':
    cfg = config.get()
    api_data = api.get_ns2_api_data(cfg["ns2_stats_api_url"])
    init()

    # Start up the server to expose the metrics.
    start_http_server(8000)
    print("Starting server on port 8000...\nhttp://localhost:8000/metrics")

    # Generate some requests.
    while True:
        update_all(api_data)
        time.sleep(cfg["metrics_update_interval_in_seconds"])
