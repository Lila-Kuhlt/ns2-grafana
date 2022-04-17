from prometheus_client import Gauge
from src.metrics._METRIC import _METRIC


class MAPS(_METRIC):
    def __init__(self):
        super().__init__(Gauge('maps', 'Total games on different maps', ['maps']))

    def update(self, api_data):
        for map_name in api_data['data']['maps']:
            total_games = api_data['data']['maps'][map_name]['total_games']

            try:
                self.METRIC.labels(map_name).set(total_games)
            except:
                continue