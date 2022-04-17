__all__ = (
    'init',
    'update_all',
    '_METRIC',
    'KD'
)

from src.metrics.KD import KD

metrics = []


def init():
    metrics.append(KD())


def update_all(api_data):
    for metric in metrics:
        metric.update(api_data)
