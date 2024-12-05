import pytest
from numeric_input import read_int, read_float

# Test for read_int function (checking valid and invalid inputs)
def test_read_int_valid(monkeypatch):
    # Simulate user input within range
    monkeypatch.setattr('builtins.input', lambda _: '5')
    result = read_int("Enter a number between 1 and 10: ", 1, 10)
    assert result == 5

def test_read_int_invalid_value(monkeypatch):
    # Simulate invalid input followed by a valid input
    monkeypatch.setattr('builtins.input', lambda _: '20')
    monkeypatch.setattr('builtins.input', lambda _: '5')
    result = read_int("Enter a number between 1 and 10: ", 1, 10)
    assert result == 5

def test_read_int_non_integer_input(monkeypatch):
    # Simulate non-integer input
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    monkeypatch.setattr('builtins.input', lambda _: '7')
    result = read_int("Enter a number between 1 and 10: ", 1, 10)
    assert result == 7

# Test for read_float function (checking valid and invalid inputs)
def test_read_float_valid(monkeypatch):
    # Simulate user input within range
    monkeypatch.setattr('builtins.input', lambda _: '5.5')
    result = read_float("Enter a number between 1.0 and 10.0: ", 1.0, 10.0)
    assert result == 5.5

def test_read_float_invalid_value(monkeypatch):
    # Simulate invalid float input followed by a valid one
    monkeypatch.setattr('builtins.input', lambda _: '20.5')
    monkeypatch.setattr('builtins.input', lambda _: '3.5')
    result = read_float("Enter a number between 1.0 and 10.0: ", 1.0, 10.0)
    assert result == 3.5

def test_read_float_non_float_input(monkeypatch):
    # Simulate non-float input
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    monkeypatch.setattr('builtins.input', lambda _: '4.0')
    result = read_float("Enter a number between 1.0 and 10.0: ", 1.0, 10.0)
    assert result == 4.0
