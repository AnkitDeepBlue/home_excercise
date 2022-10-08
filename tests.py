import pytest
from fastapi.testclient import TestClient
from server import app
from client import get_employees

client = TestClient(app)


@pytest.mark.parametrize("name, title, salary",
                         [("Name_A", "Title_A", 100), ("Name_B", "Title_B", 200), ("Name_C", "Title_C", 300)])
def test_add_multiple_employees(name, title, salary):
    for i in range(0, 3):
        response = client.post(
            "/employees",
            json={
                "name": name,
                "salary": salary,
                "title": title
            }
        )
        assert response.status_code == 200
        assert response.json()[name]['title'] == title
        assert response.json()[name]['salary'] == salary
        my_id = response.json()[name]['id']
        print(my_id)


def test_add_single_employee():
    response = client.post(
        "/employees",
        json={
            "name": "testName",
            "salary": 20000,
            "title": "testTitle"
        }
    )
    assert response.status_code == 200
    assert response.json()['testName']['title'] == 'testTitle'
    assert response.json()['testName']['salary'] == 20000


def test_delete_inexistent_employee():
    response = client.delete(
        "/employees",
        json={
            "name": "zzzzz"
        }
    )
    assert response.status_code == 200
    # In case name does not found over server we designed that it throws name back into the response, checking the same at below:
    assert response.json() == 'zzzzz'


def test_delete_employee():
    response = client.delete(
        "/employees",
        json={
            # Add the name to be deleted
            "name": "A"
        }
    )
    assert response.status_code == 200


def test_add_employee_with_existing_id():
    response = client.post(
        "/employees",
        json={
            "name": "testName",
            "salary": 20000,
            "title": "testTitle"
        }
    )
    assert response.status_code == 200

def test_add_employee_with_no_data():
    response = client.post(
        "/employees",
        json={}
    )
    assert response.status_code == 422


def test_get_all_employees():
    response = client.get("/employees")
    assert response.status_code == 200
    print(response.content)
