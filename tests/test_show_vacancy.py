from src.class_show import ShowVacancies
from src.class_vacancies import Vacancies


v = ShowVacancies("a", "b", "c", "d", "e", "f")
v1 = Vacancies("q", 3, "w", "l", "r", "n")
v2 = Vacancies("j", 2, "h", "i", "g", "k")


def test_show():
    print(v)
    assert v.currency == "c"


def test_compare():
    assert v2.salary < v1.salary
