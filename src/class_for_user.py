class ForUser:
    """Взаимодействуем с пользователем, проверяем правильность введенных данных"""
    def __init__(self, name):
        print("поиск вакансий")
        self.name = name

    def lets_talk_exp(self):
        """Узнаем есть ли опыт"""
        exp_id = ["noExperience", "between1And3", "between3And6", "moreThan6ds"]
        try:
            experience = int(input("опыт работы (выберите число)\n"
                                   " 1) нет\n"
                                   " 2) от 1 до 3 лет\n"
                                   " 3) от 3 до 6 лет\n"
                                   " 4) более 6 лет\n"))
            if isinstance(experience, str):
                raise TypeError
            if experience > len(exp_id):
                raise IndexError
            else:
                user_exp = exp_id[experience - 1]
                return user_exp
        except TypeError:
            print("В поле опыт необходимо ввести число")
            self.lets_talk_exp()
        except IndexError:
            print(f"Число в поле опыт не должно превышать {len(exp_id)}")
            self.lets_talk_exp()

    def lets_talk_emp(self):
        """Узнаем предпочитаемую занятость"""
        employment = ["full", "part", "project", "volunteer", "probation"]
        try:
            emp = int(input("занятость (выберите число)\n"
                            " 1) полная\n"
                            " 2) частичная\n"
                            " 3) проектная работа\n"
                            " 4) волонтерство\n"
                            " 5) стажировка\n"))
            if isinstance(emp, str):
                raise TypeError
            if emp > len(employment):
                raise IndexError
            else:
                user_emp = employment[emp - 1]
                return user_emp
        except TypeError:
            print("В поле занятость необходимо ввести число")
            self.lets_talk_emp()
        except IndexError:
            print(f"Число в поле опыт не должно превышать {len(employment)}")
            self.lets_talk_emp()

    @staticmethod
    def lets_talk_top():
        """Предлагаем выбрать количество вакансий"""
        n_top = int(input("введите выборку\n"))
        return n_top
