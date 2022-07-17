import json

config = {
    "ns2_stats_api_url": "http://localhost:8001/stats",

    "server_port": 8000,
    "metrics_update_interval_in_seconds": 60
}


def get():
    return config
