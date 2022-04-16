from prometheus_client import Gauge
import random

METRIC = Gauge('kd', 'KD of all players')


def init_metric():
    METRIC.labels('kid ilias').set(0)
    return 1


def get_metric():
    return METRIC


def update_metric():
    METRIC.labels('kid ilias').set(random.randint(0, 100))
    return 1
