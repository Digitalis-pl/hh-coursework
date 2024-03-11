from src.abc_class import Get
import requests


class GetResponse(Get):
    """Класс для запроса к сайту"""
    def __init__(self, name, experience, employment, top_number):
        self.experience = experience
        self.name = name
        self.employment = employment
        self.top = top_number
        self.all_vacancies = self.get_information()

    def sort_info(self) -> list:
        """Сортируем данные"""
        useful_inf = []
        counter = 0
        while counter < self.top:
            cell = {}
            counter += 1
            try:
                cell["name"] = self.get_information()["items"][counter - 1]["name"]
                cell["requirement"] = self.get_information()["items"][counter - 1]["snippet"]["requirement"]
                cell["responsibility"] = self.get_information()["items"][counter - 1]["snippet"]["responsibility"]
                cell["link"] = self.get_information()["items"][counter - 1]["apply_alternate_url"]
                try:
                    cell["start_salary"] = self.get_information()["items"][counter - 1]["salary"]["from"]
                    cell["currency"] = self.get_information()["items"][counter - 1]["salary"]["currency"]
                except TypeError:
                    cell["start_salary"] = "Зарплата не указана"
                    cell["currency"] = "Зарплата не указана"
            except IndexError:
                print("в списке больше нет вакансий")
            useful_inf.append(cell)
        return useful_inf

    def get_information(self) -> dict:
        try:
            params = {"text": f'NAME:{self.name}',
                      "experience": f"{self.experience}",
                      "per_page": f"{self.top}",
                      "area": 113,
                      "employment": f"{self.employment}"}
            response = requests.get("https://api.hh.ru/vacancies", params=params)
            if response.status_code == 200:
                return response.json()
            else:
                raise UserWarning
        except UserWarning:
            print("Что то пошло не так введите запрос заново")
