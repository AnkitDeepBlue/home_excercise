from fastapi.testclient import TestClient
from server import app
from client import get_employees

client = TestClient(app)


def test_add_employee():
    response = client.post(
        "/employees",
        json={
            "name": "testName",
            "salary": 20000,
            "title": "testTitle"
        }
    )
    assert response.status_code == 200

def test_delete_inexistent_employee():
    response = client.delete(
        "/employees",
        json={
            "name": "testName"
        }
    )
    assert response.status_code == 200
    # assert response.json().get("name") == "testName"


def test_delete_employee():
    response = client.delete(
        "/employees",
        json={
            "name": "testName_ankit"
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


def test_get_all_employees():
    response = client.get("/employees")
    assert response.status_code == 200

