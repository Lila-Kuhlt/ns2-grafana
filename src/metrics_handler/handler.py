from src.metrics_handler.metrics import KD

metrics = []


def init():
    KD.KD()


def update_all(api_data):
    for metric in metrics:
        metric.update(api_data)
