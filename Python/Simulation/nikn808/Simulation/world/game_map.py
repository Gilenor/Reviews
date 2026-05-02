from typing import Optional
import random
from world.coordinates import Coordinate
from entities.entity import Entity

DIRECTIONS_4 = ((0, 1), (0, -1), (1, 0), (-1, 0))

class GameMap:
    """Класс Карты (хранит сущности и их позиции)"""

    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        
        self._entities: dict[Coordinate, Entity] = {}
        self._entity_positions: dict[Entity, Coordinate] = {}
        
        self._empty_cells: set[Coordinate] = {Coordinate(x, y) for y in range(height) for x in range(width)}

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def is_within_bounds(self, pos: Coordinate) -> bool:
        """Проверяет, что координаты в пределах карты"""
        return 0 <= pos.x < self._width and 0 <= pos.y < self._height

    def is_empty(self, pos: Coordinate) -> bool:
        """Проверяет, что клетка пуста"""
        return self.is_within_bounds(pos) and pos in self._empty_cells

    def get_random_empty_cells(self, count: int) -> list[Coordinate]:
        """Возвращает список случайных пустых клеток"""
        if not self._empty_cells or count <= 0:
            return[]
        return random.sample(list(self._empty_cells), min(count, len(self._empty_cells)))

    def add_entity(self, pos: Coordinate, entity: Entity) -> None:
        """Добавляет сущность на карту"""
        if not self.is_within_bounds(pos):
            raise ValueError(f"Координаты {pos} вне границ карты.")
        if not self.is_empty(pos):
            raise ValueError(f"Клетка {pos} уже занята.")
        if entity in self._entity_positions:
            raise ValueError("Сущность уже находится на карте.")
        
        self._entities[pos] = entity
        self._entity_positions[entity] = pos
        self._empty_cells.remove(pos)

    def remove_entity(self, pos: Coordinate) -> None:
        """Удаляет сущность с карты"""
        if pos in self._entities:
            entity = self._entities.pop(pos)
            del self._entity_positions[entity]
            self._empty_cells.add(pos)

    def get_entity(self, pos: Coordinate) -> Optional[Entity]:
        """Возвращает сущность на указанной позиции"""
        return self._entities.get(pos)

    def get_position(self, entity: Entity) -> Optional[Coordinate]:
        """Возвращает позицию сущности"""
        return self._entity_positions.get(entity)

    def move_entity(self, from_pos: Coordinate, to_pos: Coordinate) -> None:
        """Перемещает сущность с одной позиции на другую"""
        if from_pos not in self._entities:
            raise ValueError(f"В клетке {from_pos} нет объекта.")
        if from_pos == to_pos:
            return
        if not self.is_empty(to_pos):
            raise ValueError(f"Клетка {to_pos} уже занята.")

        entity = self._entities.pop(from_pos)
        self._entities[to_pos] = entity
        self._entity_positions[entity] = to_pos
        
        self._empty_cells.add(from_pos)
        self._empty_cells.remove(to_pos)

    def get_all_entities(self) -> list[Entity]:
        return list(self._entities.values())

    def get_neighbors(self, pos: Coordinate, directions=DIRECTIONS_4) -> list[Coordinate]:
        neighbors =[]
        for direction in directions:
            neighbor = pos + direction
            if self.is_within_bounds(neighbor):
                neighbors.append(neighbor)
        return neighbors