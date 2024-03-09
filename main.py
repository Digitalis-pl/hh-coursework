from src.zapros import GetResponse
from src.class_info_saver import SaveInfo
from src.utils import form_list, sort
from src.class_for_user import ForUser

name = input("Введите вакансию\n")
fu = ForUser(name)
get_example = GetResponse(name, fu.lets_talk_exp(), fu.lets_talk_emp(), fu.lets_talk_top())
a = get_example.sort_info()
vac_list = form_list(a)
for vacancy in sort(vac_list):
    print(vacancy)
load_inf = SaveInfo(a)
