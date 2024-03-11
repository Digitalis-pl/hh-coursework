from abc import ABC, abstractmethod


class AddAbc(ABC):

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def take_info_from_data(self):
        pass

    @abstractmethod
    def __del__(self):
        pass
