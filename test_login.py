from authenticate import load_people, login


def test_load_people():
    people = load_people()
    assert len(people) == 3
    assert people[0].givenname == 'Inga'
    assert people[1].password == 'secrät'


def test_login_correct(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'geheim')
    person = login()
    captured = capsys.readouterr()
    assert person is not None
    assert person.givenname == 'Inga'

