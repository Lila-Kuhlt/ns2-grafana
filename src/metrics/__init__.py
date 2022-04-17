__all__ = (
    'init',
    'update_all',
    '_METRIC',
    'KD',
    'MAPS'
)

from src.metrics.KD import KD
from src.metrics.MAPS import MAPS

metrics = []


def init():
    metrics.append(KD())
    metrics.append(MAPS())


def update_all(api_data):
    for metric in metrics:
        metric.update(api_data)
