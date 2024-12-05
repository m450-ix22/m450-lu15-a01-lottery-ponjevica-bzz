from money import transfer_money
from person import Person


def test_transfer_money_deposit(monkeypatch):
    person = Person('Inga', 'geheim', 10.00)
    inputs = iter(['E', '20.00', 'N', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    transfer_money(person)
    assert person.balance == 30.00


def test_transfer_money_withdrawal(monkeypatch):
    person = Person('Inga', 'geheim', 20.00)
    inputs = iter(['A', '12.00', 'N', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    transfer_money(person)
    assert person.balance == 8.00
