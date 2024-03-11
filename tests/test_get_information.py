from src.class_get_information import GetResponse


s = GetResponse("разработчик", "noExperience", "part", 3)
def test_get_information():
    assert type(s.get_information()) == dict
    assert len(s.get_information()) == 10


def test_sort_info():
    assert type(s.sort_info()) == list
    assert len(s.sort_info()) == 3
