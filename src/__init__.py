from prometheus_client import start_http_server
from metrics import init_metrics, update_metrics


if __name__ == '__main__':
    init_metrics()

    # Start up the server to expose the metrics.
    start_http_server(8000)
    print("Starting server on port 8000...\nhttp://localhost:8000/metrics")

    # Generate some requests.
    while True:
        update_metrics()
