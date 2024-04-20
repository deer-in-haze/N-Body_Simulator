from abc import ABC, abstractmethod


class Settings(ABC):
    @abstractmethod
    def display(self):
        pass
