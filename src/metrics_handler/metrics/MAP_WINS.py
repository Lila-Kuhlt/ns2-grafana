from prometheus_client import Gauge
from metrics_handler._METRIC import _METRIC


class MAP_WINS(_METRIC):
    def __init__(self):
        super().__init__(Gauge('ns2_map_wins', 'Total wins on each map', ['map', 'race']))

    def update(self, api_data):
        for map_name in api_data['data']['maps']:
            alien_wins = api_data['data']['maps'][map_name]['alien_wins']
            marine_wins = api_data['data']['maps'][map_name]['marine_wins']

            try:
                self.METRIC.labels(map_name, 'alien_wins').set(alien_wins)
                self.METRIC.labels(map_name, 'marine_wins').set(marine_wins)
            except:
                continue
