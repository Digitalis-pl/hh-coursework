import pytest
from src.class_for_user import ForUser
from src.class_get_information import GetResponse


def test_lets_talk_exp(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3")
    a = ForUser("name")
    assert a.lets_talk_exp() == "between3And6"
    monkeypatch.setattr('builtins.input', lambda _: "8")
    assert a.lets_talk_exp() == None
    monkeypatch.setattr('builtins.input', lambda _: "some")
    assert a.lets_talk_emp() == None


def test_lets_talk_emp(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3")
    a = ForUser("name")
    assert a.lets_talk_emp() == "project"
    monkeypatch.setattr('builtins.input', lambda _: "8")
    assert a.lets_talk_emp() == None
    monkeypatch.setattr('builtins.input', lambda _: "some")
    assert a.lets_talk_emp() == None
