from prometheus_client import Gauge
from src.metrics_handler._METRIC import _METRIC


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
