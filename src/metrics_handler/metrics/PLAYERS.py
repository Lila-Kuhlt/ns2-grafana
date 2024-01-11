from prometheus_client import Gauge
from metrics_handler._METRIC import _METRIC


class PLAYERS(_METRIC):
    def __init__(self):
        super().__init__(Gauge('ns2_players', 'Specific stats (total_games, marines, aliens, kills, assists, deaths, kd, kda, commander) about all players', ['player_name', 'stat_type']))

    def update(self, api_data):
        for player_name in api_data['data']['users']:
            total_games = api_data['data']['users'][player_name]['total_games']
            marine_games = api_data['data']['users'][player_name]['marines']
            alien_games = api_data['data']['users'][player_name]['aliens']
            commander_games = api_data['data']['users'][player_name]['commander']
            player_games = total_games - commander_games
            kills = api_data['data']['users'][player_name]['kills']
            assists = api_data['data']['users'][player_name]['assists']
            deaths = api_data['data']['users'][player_name]['deaths']
            kd = kills / deaths if deaths > 0 else kills
            kda = (kills + assists) / deaths if deaths > 0 else (kills + assists)

            try:
                self.METRIC.labels(player_name, 'total_games').set(total_games)
                self.METRIC.labels(player_name, 'marine_games').set(marine_games)
                self.METRIC.labels(player_name, 'alien_games').set(alien_games)
                self.METRIC.labels(player_name, 'commander_games').set(commander_games)
                self.METRIC.labels(player_name, 'player_games').set(player_games)
                self.METRIC.labels(player_name, 'kills').set(kills)
                self.METRIC.labels(player_name, 'assists').set(assists)
                self.METRIC.labels(player_name, 'deaths').set(deaths)
                self.METRIC.labels(player_name, 'kd').set(kd)
                self.METRIC.labels(player_name, 'kda').set(kda)
            except:
                continue
