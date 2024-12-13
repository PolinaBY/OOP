from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass
      
class Observable(ABC):
    def __init__(self):
        self._observers: List[Observer] = []
      
    def add_observer(self, observer: Observer):
        """Добавление нового наблюдателя"""
        if observer not in self._observers:
            self._observers.append(observer)
          
    def remove_observer(self, observer: Observer):
        """Удаление наблюдателя"""
        if observer in self._observers:
            self._observers.remove(observer)
          
    def notify_observers(self):
        """Уведомление всех наблюдателей об изменении"""
        for observer in self._observers:
            observer.update()
