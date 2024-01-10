from prometheus_client import Gauge
from metrics_handler._METRIC import _METRIC


class TOTAL_WINS(_METRIC):
    def __init__(self):
        super().__init__(Gauge('ns2_total_wins', 'Total wins in all games', ['race']))

    def update(self, api_data):
        try:
            self.METRIC.labels('alien_wins').set(api_data['data']['alien_wins'])
            self.METRIC.labels('marine_wins').set(api_data['data']['marine_wins'])
            self.METRIC.labels('total_games').set(api_data['data']['total_games'])
        except:
            print()


