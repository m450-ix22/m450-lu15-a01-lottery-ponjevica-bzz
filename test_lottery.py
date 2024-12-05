from lottery import create_ticket, select_numbers
from person import Person
from ticket import Ticket


def test_create_ticket_sufficient_balance(monkeypatch):
    person = Person('Inga', 'geheim', 10.00)

    inputs = iter(['5', '10', '15', '20', '25', '30', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    create_ticket(person)

    assert person.balance == 8.00


def test_create_ticket_insufficient_balance(monkeypatch):
    person = Person('Inga', 'geheim', 1.00)

    inputs = iter(['5', '10', '15', '20', '25', '30', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    create_ticket(person)

    assert person.balance == 1.00


def test_select_numbers(monkeypatch):
    ticket = Ticket(0, [])

    inputs = iter(['5', '10', '15', '20', '25', '30', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    select_numbers(ticket)

    assert len(ticket.numbers) == 6
    assert all(1 <= num <= 42 for num in ticket.numbers)
    assert len(set(ticket.numbers)) == 6
    assert ticket.joker == 3
