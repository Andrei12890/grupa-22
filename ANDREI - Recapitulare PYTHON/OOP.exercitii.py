# class QuadrupedAnimal:
#     legs_no = 4
#
#     @staticmethod
#     def speak():
#         pass
#
#
# class Pet:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     def change_name(self, name):
#         self.__name = name

class FibonacciIterator:

    def __iter__(self):
        self.value = 1
        self.prev = 0
        return self

    def __next__(self):
        value = self.value
        self.value += self.prev
        self.prev = value
        return value
