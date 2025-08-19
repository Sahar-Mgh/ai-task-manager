import pytest
from app import app # Imports the app we created

@pytest.fixture
def client():
    # Create a test client for our app
    with app.test_client() as client:
        yield client

def test_index_page_loads(client):
    """Test that the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    # Check if the title "My Tasks" is on the page
    assert b"My Tasks" in response.data

def test_add_task(client):
    """Test that a new task can be added."""
    # Send a POST request, simulating a user submitting the form
    response = client.post('/', data={'task': 'A New Test Task'}, follow_redirects=True)
    
    # Check that the page is still okay
    assert response.status_code == 200
    # Crucially, check if our new task now appears in the page's content
    assert b"A New Test Task" in response.data

    # ... (previous test code) ...

def test_mark_task_as_done(client):
    """Test that a task can be marked as done."""
    # First, add a task to ensure the list isn't empty
    client.post('/', data={'task': 'Task to be marked done'}, follow_redirects=True)
    
    # Now, simulate clicking the 'Mark as Done' link for the first task (ID 0)
    response = client.get('/done/0', follow_redirects=True)
    
    assert response.status_code == 200
    # Check if the task text is now wrapped in a strikethrough style
    assert b'<span style="text-decoration: line-through;">' in response.data