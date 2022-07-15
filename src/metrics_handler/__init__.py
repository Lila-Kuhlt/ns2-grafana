__all__ = (
    'init',
    'update_all',
    '_METRIC',
    'metrics'
)

from metrics_handler import metrics
from importlib import import_module
from threading import Thread

metrics_list = []


def init():
    for metric in metrics.__all__:
        module = import_module('metrics_handler.metrics.' + metric)
        metric_cls = getattr(module, metric)
        metrics_list.append(metric_cls())


def update_all(api_data):
    for metric in metrics_list:
        try:
            Thread(target=metric.update, args=(api_data,)).start()
        except:
            print("Update_All error")

