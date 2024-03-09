class ShowVacancies:
    """Клас для отображения информации"""
    def __init__(self, name, salary, currency, link, requirements, responsibility):
        self.name = name
        self.salary = salary
        self.currency = currency
        self.link = link
        self.requirement = requirements
        self.responsibility = responsibility

    def __str__(self):
        return f"{self.name}\n{self.salary}\n{self.currency}\n{self.requirement}\n{self.responsibility}\n{self.link}\n"
