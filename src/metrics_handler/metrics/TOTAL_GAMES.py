from prometheus_client import Gauge
from metrics_handler._METRIC import _METRIC


class TOTAL_GAMES(_METRIC):
    def __init__(self):
        super().__init__(Gauge('ns2_total_games', 'Total games'))

    def update(self, api_data):
        try:
            self.METRIC.set(api_data['data']['total_wins'])
        except:
            print()


