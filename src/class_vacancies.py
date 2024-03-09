from src.class_show import ShowVacancies


class Vacancies(ShowVacancies):
    """Инициализируем объекты"""
    name: str
    description: str
    salary: float
    link: str
    requirement: str
    responsibility: str

    def __init__(self, name, salary, currency, link, requirements, responsibility):
        super().__init__(name, salary, currency, link, requirements, responsibility)

    def __lt__(self, other):
        if isinstance(self.salary, str):
            return self.salary < other.salary
