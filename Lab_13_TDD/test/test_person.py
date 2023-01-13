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

def test_People_constructor():
    people = People(testdata1)
    assert people[0] == Person("Piotr", "Wolnik", 22)
    assert people[1] == Person("Michael", "Crazy", 24)
    assert people[2] == Person("Joanna", "Phalaphel", 23)


testdata = ["Wolnik, Piotr -> 22", "Crazy, Michael -> 24"]
@pytest.mark.parametrize('sample', testdata)
def test_str_method(sample):
    people = People([Person("Piotr", "Wolnik", 22), Person("Michael", "Crazy", 24)])
    assert str(people[0]) == testdata[0]
    assert str(people[1]) == testdata[1]
    