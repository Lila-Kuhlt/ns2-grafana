# ns2-grafana
This project defines metrics for [Prometheus](https://prometheus.io/) from game data of the Game [NS2](https://store.steampowered.com/app/4920/Natural_Selection_2/) provided by `ns2-stat-api` from project [NS2-Stat](https://github.com/Lila-Kuhlt/ns2-stat).

## Setup
* Run `pip install -r requirements.txt`
* Go into file `/src/util/config.py` and set config values
  - `ns2_stats_api_url` is the location for the running `ns2-stat-api` instance form project [NS2-Stat](https://github.com/Lila-Kuhlt/ns2-stat)
  - `server-port` is the hosting location where Prometheus can scrape the data

## Run
Run `python src/__init__.py`

## Externals
### NS2-Stat
Note that you have to run [NS2-Stat](https://github.com/Lila-Kuhlt/ns2-stat) that provided the game data as api. Just go to the project and read their docu for help.

### Prometheus Config
Add the following configuration in the `scrape_configs`-block into your `prometheus.yml` file. The `targets` port has to be the same as the `server-port` above.

```YML
  - job_name: "ns2"
    
    static_configs:
      - targets: ["localhost:8000"]
```

### Grafana Dashboard
If you want to use [Grafana](https://grafana.com/) to virtualise the metrics, you can find a ready-made dashboard in `grafana/dashboard.json`
