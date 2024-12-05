import pytest

from person import Person


def test_person_initialization():
    person = Person('Paula', 'geheim', 14.00)
    assert person.givenname == 'Paula'
    assert person.password == 'geheim'
    assert person.balance == 14.00


def test_person_balance_invalid():
    with pytest.raises(ValueError):
        person = Person('Paula', 'geheim', 'some value')


def test_person_balance_valid():
    person = Person('Paula', 'geheim', 20.00)
    person.balance = 50.00
    assert person.balance == 50.00
