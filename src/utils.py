from src.class_vacancies import Vacancies


def form_list(some):
    """Формируем список"""
    our_list = []
    for i in some:
        our_list.append(Vacancies(i["name"],
                                  i["start_salary"],
                                  i["currency"],
                                  i["link"],
                                  i["requirement"],
                                  i["responsibility"]))
    return our_list


def sort(vac_list):
    """Сортируем вакансии по зарплате"""
    only_no_salary = []
    for x in vac_list:
        if isinstance(x.salary, str):
            only_no_salary.append(x)
    only_int = list(set(vac_list) - set(only_no_salary))
    sorted_only_int = sorted(only_int, key=lambda vacancies: vacancies.salary)
    sorted_vac_list = sorted_only_int + only_no_salary
    return sorted_vac_list
