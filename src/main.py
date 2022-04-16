from prometheus_client import Gauge, start_http_server
import random

# Create a metric to track time spent and requests made.
KD = Gauge('kd', 'KD of all players', ['player'])


def update_metric():
    KD.labels('kid ilias').set(random.randint(0, 100))
    KD.labels('niklas').set(random.randint(0, 100))
    KD.labels('blueblood').set(random.randint(0, 100))
    return 1


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start(8000)
    print("Starting server on port 8000...\nhttp://localhost:8000/metrics")

    # Generate some requests.
    while True:
        update_metric()
