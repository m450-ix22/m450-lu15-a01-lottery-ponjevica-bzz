import pytest

import main


@pytest.fixture
def mock_functions(monkeypatch):

    def dummy_login():
        pass

    def dummy_transfer(person):
        pass

    def dummy_select_menu():
        print('Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden')
        return input('')

    def dummy_ticket(person):
        pass

    monkeypatch.setattr(main, 'login', dummy_login)
    monkeypatch.setattr(main, 'transfer_money', dummy_transfer)
    monkeypatch.setattr(main, 'select_menu', dummy_select_menu)
    monkeypatch.setattr(main, 'create_ticket', dummy_ticket)


def test_main_exit(capsys, monkeypatch, mock_functions):
    inputs = iter(['Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'


def test_main_money(capsys, monkeypatch, mock_functions):
    inputs = iter(['A', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n' \
                     'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'


def test_main_ticket(capsys, monkeypatch, mock_functions):
    inputs = iter(['B', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n' \
                     'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'


def test_main_exit(capsys, monkeypatch, mock_functions):
    inputs = iter(['Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main.main()
    output = capsys.readouterr().out

    assert 'Beenden' in output


def test_main_money(capsys, monkeypatch, mock_functions):
    inputs = iter(['A', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main.main()
    output = capsys.readouterr().out

    assert output.count('Lotto') == 4
    assert 'Ein- und Auszahlungen' in output


def test_main_ticket(capsys, monkeypatch, mock_functions):
    inputs = iter(['B', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main.main()
    output = capsys.readouterr().out

    assert output.count('Lotto') == 4
    assert 'Lottotipps abgeben' in output
