import pytest
from src.task_5_1 import generate_users


@pytest.fixture
def first_names():
    return ['John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia', 'James', 'Ava', 'Alexander', 'Mia']


@pytest.fixture
def last_names():
    return ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']


@pytest.fixture
def cities():
    return ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego',
              'Dallas', 'San Jose']


def test_generate_users(first_names, last_names, cities):
    users = generate_users(first_names, last_names, cities)
    user = next(users)
    assert user["first_name"] in first_names
    assert user["last_name"] in last_names
    assert user["age"] in range(18, 65)
    assert user["city"] in cities