import unittest
import json
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from todo_app import create_app, mongo
from todo_app.models.todo import Todo

class TestTodoRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        cls.app = create_app()
        cls.app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo_app_test'
        cls.client = cls.app.test_client()

    def setUp(self):
        """Run before each test"""
        with self.app.app_context():
            Todo.clear_all()

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests"""
        with cls.app.app_context():
            Todo.clear_all()
            # Close MongoDB connection
            mongo.cx.close()

    def test_create_todo_success(self):
        """Test creating a new todo with valid data"""
        response = self.client.post('/api/todos',
            json={
                'title': 'Test Todo',
                'category': 'Test',
                'due_date': (datetime.utcnow() + timedelta(days=1)).isoformat()
            }
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Todo')
        self.assertEqual(data['category'], 'Test')
        self.assertFalse(data['completed'])

    def test_create_todo_missing_title(self):
        """Test creating a todo without title should fail"""
        response = self.client.post('/api/todos',
            json={
                'category': 'Test'
            }
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Title is required')

    def test_create_todo_invalid_date(self):
        """Test creating a todo with invalid date format"""
        response = self.client.post('/api/todos',
            json={
                'title': 'Test Todo',
                'due_date': 'invalid-date'
            }
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Invalid due date format')

    def test_get_todos_empty(self):
        """Test getting todos when none exist"""
        response = self.client.get('/api/todos')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 0)

    def test_get_todos_with_data(self):
        """Test getting all todos when they exist"""
        # Create test todos
        self.client.post('/api/todos',
            json={'title': 'Todo 1', 'category': 'Test'}
        )
        self.client.post('/api/todos',
            json={'title': 'Todo 2', 'category': 'Test'}
        )
        
        response = self.client.get('/api/todos')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['title'], 'Todo 1')
        self.assertEqual(data[1]['title'], 'Todo 2')

    def test_get_todos_by_category(self):
        """Test filtering todos by category"""
        self.client.post('/api/todos',
            json={'title': 'Work Todo', 'category': 'Work'}
        )
        self.client.post('/api/todos',
            json={'title': 'Personal Todo', 'category': 'Personal'}
        )
        
        response = self.client.get('/api/todos?category=Work')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Work Todo')

    def test_update_todo_success(self):
        """Test updating a todo successfully"""
        # Create a todo first
        create_response = self.client.post('/api/todos',
            json={'title': 'Test Todo'}
        )
        todo_id = json.loads(create_response.data)['id']
        
        # Update the todo
        response = self.client.put(f'/api/todos/{todo_id}',
            json={
                'title': 'Updated Todo',
                'completed': True,
                'category': 'Updated Category'
            }
        )
        self.assertEqual(response.status_code, 200)
        
        # Verify the update
        get_response = self.client.get('/api/todos')
        data = json.loads(get_response.data)
        self.assertEqual(data[0]['title'], 'Updated Todo')
        self.assertTrue(data[0]['completed'])
        self.assertEqual(data[0]['category'], 'Updated Category')

    def test_update_todo_invalid_id(self):
        """Test updating a todo with invalid ID"""
        response = self.client.put('/api/todos/invalid_id',
            json={'title': 'Updated Todo'}
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_todo_success(self):
        """Test deleting a todo successfully"""
        # Create a todo first
        create_response = self.client.post('/api/todos',
            json={'title': 'Test Todo'}
        )
        todo_id = json.loads(create_response.data)['id']
        
        # Delete the todo
        response = self.client.delete(f'/api/todos/{todo_id}')
        self.assertEqual(response.status_code, 200)
        
        # Verify it's deleted
        get_response = self.client.get('/api/todos')
        data = json.loads(get_response.data)
        self.assertEqual(len(data), 0)

    def test_delete_todo_invalid_id(self):
        """Test deleting a todo with invalid ID"""
        response = self.client.delete('/api/todos/invalid_id')
        self.assertEqual(response.status_code, 404)

    def test_get_categories_empty(self):
        """Test getting categories when none exist"""
        response = self.client.get('/api/categories')
        self.assertEqual(response.status_code, 200)
        categories = json.loads(response.data)
        self.assertEqual(len(categories), 0)

    def test_get_categories_with_data(self):
        """Test getting categories when they exist"""
        # Create todos with different categories
        self.client.post('/api/todos',
            json={'title': 'Todo 1', 'category': 'Work'}
        )
        self.client.post('/api/todos',
            json={'title': 'Todo 2', 'category': 'Personal'}
        )
        self.client.post('/api/todos',
            json={'title': 'Todo 3', 'category': 'Work'}
        )
        
        response = self.client.get('/api/categories')
        self.assertEqual(response.status_code, 200)
        categories = json.loads(response.data)
        self.assertEqual(len(categories), 2)
        self.assertIn('Work', categories)
        self.assertIn('Personal', categories)

    def test_get_overdue_todos(self):
        """Test getting overdue todos"""
        # Create an overdue todo
        yesterday = datetime.utcnow() - timedelta(days=1)
        self.client.post('/api/todos',
            json={
                'title': 'Overdue Todo',
                'due_date': yesterday.isoformat()
            }
        )
        
        # Create a future todo
        tomorrow = datetime.utcnow() + timedelta(days=1)
        self.client.post('/api/todos',
            json={
                'title': 'Future Todo',
                'due_date': tomorrow.isoformat()
            }
        )
        
        response = self.client.get('/api/todos/overdue')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Overdue Todo')

if __name__ == '__main__':
    unittest.main() 