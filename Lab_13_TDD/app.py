from typing import List

class Person:
    def __init__(self, name: str = "Piotr", surname: str = "Wolnik", age: int = 22):
        self.name = name
        self.surname = surname
        self.age = age
    
    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.surname == __o.surname and self.age == __o.age

    def __str__(self):
        return f"{self.surname}, {self.name} -> {self.age}"

class People:
    def __init__(self, group_of_people: list):
        self.people = []
        for person in group_of_people:
            self.people.append(person)

    def __getitem__(self, key):
        return self.people[key]

    def __str__(self):
        string = ""
        for person in self.people:
            string += f"{person}\n"
        return string