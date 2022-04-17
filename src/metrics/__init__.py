__all__ = (
    'update_metrics',
    'init_metrics',
    'KD',
    'KDA',
    'MAPS',
)


def init_metrics():
    for metric in __all__:
        metric.init()


def update_metrics():
    for metric in __all__:
        metric.update()
