from prometheus_client import Gauge
import random

METRIC = Gauge('kd', 'KD of all players')


def init():
    METRIC.labels('kid ilias').set(0)
    return 1


def get():
    return METRIC


def update():
    METRIC.labels('kid ilias').set(random.randint(0, 100))
    return 1


# from prometheus_client import Gauge, start_http_server
# import random
#
# # Create a metrics to track time spent and requests made.
# KD = Gauge('kd', 'KD of all players', ['player'])
#
#
# def update_metric():
#     KD.labels('kid ilias').set(random.randint(0, 100))
#     KD.labels('niklas').set(random.randint(0, 100))
#     KD.labels('blueblood').set(random.randint(0, 100))
#     return 1
