from prometheus_client import Gauge
from metrics_handler._METRIC import _METRIC


class MAPS(_METRIC):
    def __init__(self):
        super().__init__(Gauge('ns2_maps', 'Total games on different maps', ['map']))

    def update(self, api_data):
        for map_name in api_data['data']['maps']:
            total_games = api_data['data']['maps'][map_name]['total_games']

            try:
                self.METRIC.labels(map_name).set(total_games)
            except:
                continue
