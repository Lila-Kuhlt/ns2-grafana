from prometheus_client import Gauge
from src.metrics_handler._METRIC import _METRIC


class KDA(_METRIC):
    def __init__(self):
        super().__init__(Gauge('kda', 'KDA of all players', ['player']))

    def update(self, api_data):
        for player in api_data['data']['users']:
            kd = api_data['data']['users'][player]['kda']

            try:
                self.METRIC.labels(player).set(kd)
            except:
                continue
