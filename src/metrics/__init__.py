__all__ = (
    'init',
    'update_all',
    '_METRIC',
    'KD',
    'MAPS'
)

from src.metrics.KD import KD
from src.metrics.MAPS import MAPS
from src.metrics.TOTAL_WINS import TOTAL_WINS
from src.metrics.MAP_WINS import MAP_WINS

metrics = []


def init():
    metrics.append(KD())
    metrics.append(MAPS())
    metrics.append(TOTAL_WINS())
    metrics.append(MAP_WINS())


def update_all(api_data):
    for metric in metrics:
        try:
            metric.update(api_data)
        except:
            print("Update All error")
