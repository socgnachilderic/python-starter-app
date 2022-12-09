def hello() -> str:
    return "Hello world!"


def world() -> str:
    return "world"


class Calculator:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y
        self._result = 0

    def add(self):
        self._result = self._x + self._y

    def get_result(self) -> float:
        return self._result
