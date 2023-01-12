from app import *
import pytest

def test_Person_constructor():
    person = Person("Piotr", "Wolnik", 22)
    assert person.name == "Piotr"
    assert person.surname == "Wolnik"
    assert person.age == 22

testdata1 = [
        Person("Piotr", "Wolnik", 22), 
        Person("Michael", "Crazy", 24), 
        Person("Joanna", "Phalaphel", 23)
]

@pytest.mark.parametrize('sample', testdata1)
def test_People_constructor(sample):
    people = People(sample)
    assert people[0] == Person("Piotr", "Wolnik", 22)
    assert people[1] == Person("Michael", "Crazy", 24)
    assert people[2] == Person("Joanna", "Phalaphel", 23)



