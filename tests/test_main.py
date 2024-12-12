from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    
    response = client.post("/api/tasks/", json={
        "title": "Test Task",
        "description": "This is a test ",
        "priority": 3
    })

    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_get_tasks():
    
    response = client.get("/api/tasks/")
    assert response.status_code == 200
    assert "tasks" in response.json()

def test_update_task():
    
    create_response = client.post("/api/tasks/", json={
        "title": "Update Test",
        "description": "This task will be updated",
        "priority": 2
    })

    task_id = create_response.json()["id"]

    update_response = client.put(f"/api/tasks/{task_id}", json={
        "title": "Updated Task",
        "priority": 4
    })
    
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Updated Task"
    assert update_response.json()["priority"] == 4
