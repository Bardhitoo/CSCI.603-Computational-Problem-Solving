class Ball:
    __slots__ = "name", "cord_length", "weight", "radius"

    def __init__(self, name: str, cord_length: int, radius: int, weight: int):
        self.name = name
        self.cord_length = cord_length
        self.radius = radius
        self.weight = weight

    def __str__(self):
        return f"{self.name}"

    def get_weight(self):
        return self.weight

    @staticmethod
    def is_balanced():
        return True

    def width(self):
        return self.radius