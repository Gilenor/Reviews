from abc import ABC, abstractmethod, abstractproperty


class Destroyable(ABC):
    @abstractproperty
    def is_alive(self) -> bool:
        return True

    @abstractmethod
    def take_damage(self, amount: int):
        pass
