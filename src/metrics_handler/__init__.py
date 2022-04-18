__all__ = (
    'init',
    'update_all',
    '_METRIC',
    'metrics'
)

from src.metrics_handler import metrics
from importlib import import_module

metrics_list = []


def init():
    for metric in metrics.__all__:
        module = import_module('src.metrics_handler.metrics.' + metric)
        metric_cls = getattr(module, metric)
        metrics_list.append(metric_cls())


def update_all(api_data):
    for metric in metrics_list:
        try:
            metric.update(api_data)
        except:
            print("Update_All error")

