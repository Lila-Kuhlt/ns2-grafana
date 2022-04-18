from prometheus_client import Gauge
from src.metrics_handler._METRIC import _METRIC


class PLAYERS(_METRIC):
    def __init__(self):
        super().__init__(Gauge('players', 'Total wins on each map', ['name', 'kda_type']))

    def update(self, api_data):
        for player_name in api_data['data']['users']:
            kills = api_data['data']['users'][player_name]['kills']
            assists = api_data['data']['users'][player_name]['assists']
            deaths = api_data['data']['users'][player_name]['deaths']

            try:
                self.METRIC.labels(player_name, 'kills').set(kills)
                self.METRIC.labels(player_name, 'assists').set(assists)
                self.METRIC.labels(player_name, 'deaths').set(deaths)
            except:
                continue