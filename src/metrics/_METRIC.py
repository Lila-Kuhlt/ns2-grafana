from abc import ABC, abstractmethod


class _METRIC(ABC):
    def __init__(self, metric):
        self.METRIC = metric

    def get(self):
        return self.METRIC

    @abstractmethod
    def update(self, api_data):
        ...
