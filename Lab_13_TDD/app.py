from typing import List

class GetAttr(type):
    def __getitem__(cls, x):
        return getattr(cls, x)

class Person:
    __metaclass__ = GetAttr
    def __init__(self, name: str = "Piotr", surname: str = "Wolnik", age: int = 22):
        self.name = name
        self.surname = surname
        self.age = age
    
    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.surname == __o.surname and self.age == __o.age


class People:
    def __init__(self, group_of_people: list):
        self.people = group_of_people

    def __getitem__(self, key):
        return self.people[key]

# class PersonClassIter:    
    
#     def __init__(self, PeopleGroup):
#         self._group_of_people = PeopleGroup.people
#         self._group_of_people_size = len(self._group_of_people)
#         self._current_index = 0    
        
#         def __iter__(self):
#             return self    
        
#         def __next__(self):
#             if self._current_index < self._group_of_people_size:
#                 person = self._lect[self._current_index] 
#             else:
#                 person = self._group_of_people[self._current_index]
#                 self._current_index += 1
#             return person        
#             raise StopIteration