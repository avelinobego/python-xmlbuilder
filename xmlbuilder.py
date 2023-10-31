from collections import namedtuple
from typing import Any, Type


class element:
    pass


class element:
    def __init__(self, _name: str = None, value: any = None) -> None:
        self._name = _name
        self._value = value
        self._lines = []
        self._elements = []

    def value(self, val: any = None) -> str:
        if val:
            self._value = val
        return val

    def __str__(self) -> str:
        return "".join(self._lines)

    def __getattribute__(self, __name: str) -> Any:
        if __name.startswith("_"):
            return super().__getattribute__(__name)

        if __name in dir(self):
            return super().__getattribute__(__name)

        def result(value: any = None):
            self._elements.append(element(__name, value))
            return self

        return result

    def build(self) -> Type[element]:
        self._lines.clear()
        self._lines.append(self._open_tag(self._name))
        self._lines.append(self._close_tag(self._name))

    def _open_tag(self, name: str) -> str:
        return f"<{name}>"

    def _close_tag(self, name: str) -> str:
        return f"</{name}>"
