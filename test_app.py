import pytest
from app import app, db, Task

@pytest.fixture
def client():
    # --- SETUP FOR TESTING ---
    # Configure the app for testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Use an in-memory DB
    
    # Create a test client
    with app.test_client() as client:
        # Establish an application context
        with app.app_context():
            # Create the database tables
            db.create_all()
        
        yield client # This is where the test runs
        
        # --- TEARDOWN ---
        with app.app_context():
            # Drop all tables after the test is done
            db.drop_all()

def test_index_page_loads(client):
    """Test that the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"My Tasks" in response.data

def test_add_task(client):
    """Test that a new task can be added via POST and appears on the page."""
    response = client.post('/', data={'task': 'A New DB Task'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"A New DB Task" in response.data

def test_mark_task_as_done(client):
    """Test that a task can be marked as done."""
    # First, create a task in the test database
    with app.app_context():
        new_task = Task(text='Task to be marked done')
        db.session.add(new_task)
        db.session.commit()
        task_id = new_task.id
    
    # Now, simulate clicking the 'Mark as Done' link
    response = client.get(f'/done/{task_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'<span style="text-decoration: line-through;">' in response.data

def test_delete_task(client):
    """Test that a task can be deleted."""
    with app.app_context():
        new_task = Task(text='Task to be deleted')
        db.session.add(new_task)
        db.session.commit()
        task_id = new_task.id

    response = client.get(f'/delete/{task_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b"Task to be deleted" not in response.data