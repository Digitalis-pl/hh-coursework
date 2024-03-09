import json


class SaveInfo:
    """Класс для сохранения информации в json"""

    def __init__(self, info):
        self.info = info
        self.save_info()

    def save_info(self):
        with open('DATA/data.json', "w", encoding="utf-8") as f:
            f.write(json.dumps(self.info, ensure_ascii=False, indent=4))
