from dataclasses import dataclass



@dataclass(frozen=True)
class Coordinate:
    """Неизменяемый класс координат для работы с сеткой карты"""
    x: int
    y: int

    def __add__(self, value) -> "Coordinate":
        if isinstance(value, Coordinate):
            return Coordinate(self.x + value.x, self.y + value.y)
        if isinstance(value, tuple) and len(value) == 2:
            return Coordinate(self.x + value[0], self.y + value[1])
        return NotImplemented
