from menu import show_menu, select_menu


def test_show_menu(capsys):
    show_menu()
    captured = capsys.readouterr().out
    assert 'Lotto' in captured
    assert '---------' in captured
    assert 'A) Konto Ein- und Auszahlungen tätigen' in captured
    assert 'B) Lottotipps abgeben' in captured
    assert 'Z) Beenden' in captured


def test_select_menu_valid_choice(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'A')
    result = select_menu()
    assert result == 'A'


def test_select_menu_invalid_choice(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'C')
    monkeypatch.setattr('builtins.input', lambda _: 'A')
    result = select_menu()
    assert result == 'A'


def test_select_menu_multiple_invalid_choices(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'C')
    monkeypatch.setattr('builtins.input', lambda _: 'D')
    monkeypatch.setattr('builtins.input', lambda _: 'A')
    result = select_menu()
    assert result == 'A'
