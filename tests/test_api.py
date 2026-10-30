from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_exams():
    response = client.get("/exams/")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "group_id": 1,
            "teacher_id": 1,
            "duration": 10,
            "start_time": "2026-03-30T19:30:00",
            "end_time": "2026-03-30T21:30:00",
        }
    ]


def test_get_groups():
    response = client.get("/groups/")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Group 1", "count_students": 30},
        {"id": 2, "name": "Group 2", "count_students": 25},
        {"id": 3, "name": "Group 3", "count_students": 20},
    ]


def test_get_students():
    response = client.get("/students/")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "full_name": "Abdusalimova Sarvinoz",
            "age": 18,
            "phone_number": "+998777777777",
            "email": "abdusalimova@example.com",
        },
        {
            "id": 2,
            "full_name": "Rahmonaliyev Izzatbek ",
            "age": 20,
            "phone_number": "+998770000000",
            "email": "rahmonaliyev@example.com",
        },
    ]


def test_get_submissions():
    response = client.get("/submissions/")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "deadline": "2026-03-16T21:00:00", "grade": 4.5},
        {"id": 2, "deadline": "2026-03-17T21:00:00", "grade": 3.0},
    ]


def test_get_teachers():
    response = client.get("/teachers/")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "full_name": "Abdullayev Askar",
            "phone_number": "+998911111111",
            "email": "abdullayevaskar@example.com",
        }
    ]
