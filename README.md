# ns2-grafana
This project defines metrics for [Prometheus](https://prometheus.io/) from game data of the Game [NS2](https://store.steampowered.com/app/4920/Natural_Selection_2/) provided by `ns2-stat-api` from project [NS2-Stat](https://github.com/Lila-Kuhlt/ns2-stat).

## Setup
* Run `pip install -r requirements.txt`
* Go into file `/src/util/config.py` and set config values
  - `ns2_stats_api_url` is the location for the running `ns2-stat-api` instance form project [NS2-Stat](https://github.com/Lila-Kuhlt/ns2-stat)
  - `server-port` is the hosting location where Prometheus can scrape the data


## Run
Run `python src/__init__.py`
