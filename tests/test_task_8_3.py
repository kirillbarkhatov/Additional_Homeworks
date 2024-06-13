import pytest

from src.task_8_3 import shorts


def test_shorts():
    @shorts(3, symb="4")
    def text():
        return '''aaaaaaaaaaaaaaaaaaaaaa bbbbbbbb ccc ddddddddddddddddd'''


    result = text()
    assert result == 'aaa4 bbb4 ccc ddd4'