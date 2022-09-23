import pytest
from main import RangeError, category
inputs = iter([2,6])
def fake_input(prompt):
    return next(inputs)
class TestInt:
    def  test_valid(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_input)
        assert category() == 2
    def test_above_range(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_input)
        with pytest.raises(RangeError):
            category()

  