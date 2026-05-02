from entities.entity import Entity
from entities.destroyable import Destroyable


class Grass(Entity, Destroyable):
    """Ресурс для травоядных"""

    def __init__(self):
        self._is_alive = True

    @property
    def is_alive(self) -> bool:
        return self._is_alive

    def take_damage(self, amount: int=0):
        self._is_alive = False


class Rock(Entity):
    """Статичное препятствие"""


class Tree(Entity):
    """Статичное препятствие"""
