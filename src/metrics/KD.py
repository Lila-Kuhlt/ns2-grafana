from prometheus_client import Gauge
from src.metrics._METRIC import _METRIC
from numbers import Number


class KD(_METRIC):
    def __init__(self):
        super().__init__(Gauge('kd', 'KD of all players', ['player']))

    def update(self, api_data):
        for player in api_data['data']['users']:
            kd = api_data['data']['users'][player]['kd']

            try:
                self.METRIC.labels(player).set(kd)
            except:
                continue


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
