from prometheus_client import Gauge
from src.metrics._METRIC import _METRIC


class TOTAL_WINS(_METRIC):
    def __init__(self):
        super().__init__(Gauge('total_wins', 'Total wins in all games', ['race']))

    def update(self, api_data):
        try:
            self.METRIC.labels('alien_wins').set(api_data['data']['alien_wins'])
            self.METRIC.labels('marine_wins').set(api_data['data']['marine_wins'])
        except:
            print()


