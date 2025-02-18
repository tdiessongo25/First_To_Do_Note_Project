from flask import Blueprint, jsonify, request
from bson.objectid import ObjectId
from bson.errors import InvalidId
from datetime import datetime
from todo_app.models.todo import Todo

todos = Blueprint('todos', __name__)

def validate_object_id(todo_id):
    """Validate and convert string ID to ObjectId"""
    try:
        return ObjectId(todo_id)
    except InvalidId:
        return None

@todos.route('/api/todos', methods=['GET'])
def get_todos():
    category = request.args.get('category')
    todos_list = Todo.get_by_category(category) if category else Todo.get_all()
    
    return jsonify([{
        'id': str(todo['_id']),
        'title': todo['title'],
        'category': todo['category'],
        'due_date': todo['due_date'].isoformat() if todo.get('due_date') else None,
        'completed': todo['completed'],
        'created_at': todo['created_at'].isoformat()
    } for todo in todos_list])

@todos.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    # Parse due_date if provided
    due_date = None
    if 'due_date' in data:
        try:
            due_date = datetime.fromisoformat(data['due_date'])
        except ValueError:
            return jsonify({'error': 'Invalid due date format'}), 400
    
    todo = Todo(
        title=data['title'],
        category=data.get('category'),
        due_date=due_date,
        completed=data.get('completed', False)
    )
    result = todo.save()
    
    return jsonify({
        'id': str(result.inserted_id),
        'title': todo.title,
        'category': todo.category,
        'due_date': todo.due_date.isoformat() if todo.due_date else None,
        'completed': todo.completed,
        'created_at': todo.created_at.isoformat()
    }), 201

@todos.route('/api/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Validate todo_id
    object_id = validate_object_id(todo_id)
    if not object_id:
        return jsonify({'error': 'Invalid todo ID format'}), 404
        
    updates = {}
    if 'title' in data:
        updates['title'] = data['title']
    if 'category' in data:
        updates['category'] = data['category']
    if 'completed' in data:
        updates['completed'] = data['completed']
    if 'due_date' in data:
        try:
            updates['due_date'] = datetime.fromisoformat(data['due_date'])
        except ValueError:
            return jsonify({'error': 'Invalid due date format'}), 400
    
    result = Todo.update(object_id, updates)
    if result.modified_count:
        return jsonify({'message': 'Todo updated successfully'})
    return jsonify({'error': 'Todo not found'}), 404

@todos.route('/api/categories', methods=['GET'])
def get_categories():
    """Get list of all categories"""
    categories = Todo.get_categories()
    return jsonify(list(filter(None, categories)))  # Filter out None values

@todos.route('/api/todos/overdue', methods=['GET'])
def get_overdue_todos():
    """Get all overdue todos"""
    todos_list = Todo.get_overdue()
    return jsonify([{
        'id': str(todo['_id']),
        'title': todo['title'],
        'category': todo['category'],
        'due_date': todo['due_date'].isoformat(),
        'completed': todo['completed'],
        'created_at': todo['created_at'].isoformat()
    } for todo in todos_list])

@todos.route('/api/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    # Validate todo_id
    object_id = validate_object_id(todo_id)
    if not object_id:
        return jsonify({'error': 'Invalid todo ID format'}), 404
        
    result = Todo.delete(object_id)
    if result.deleted_count:
        return jsonify({'message': 'Todo deleted successfully'})
    return jsonify({'error': 'Todo not found'}), 404 