from datetime import datetime
from todo_app import mongo

class Todo:
    def __init__(self, title, category=None, due_date=None, completed=False):
        self.title = title
        self.category = category
        self.due_date = due_date
        self.completed = completed
        self.created_at = datetime.utcnow()
    
    def save(self):
        return mongo.db.todos.insert_one({
            'title': self.title,
            'category': self.category,
            'due_date': self.due_date,
            'completed': self.completed,
            'created_at': self.created_at
        })
    
    @staticmethod
    def get_all():
        """Get all todos"""
        return mongo.db.todos.find()
    
    @staticmethod
    def get_by_category(category):
        return mongo.db.todos.find({'category': category})
    
    @staticmethod
    def get_by_id(todo_id):
        return mongo.db.todos.find_one({'_id': todo_id})
    
    @staticmethod
    def delete(todo_id):
        return mongo.db.todos.delete_one({'_id': todo_id})
    
    @staticmethod
    def update(todo_id, updates):
        return mongo.db.todos.update_one(
            {'_id': todo_id},
            {'$set': updates}
        )
    
    @staticmethod
    def get_categories():
        """Get list of unique categories"""
        return mongo.db.todos.distinct('category')
    
    @staticmethod
    def get_overdue():
        """Get all overdue todos"""
        return mongo.db.todos.find({
            'due_date': {'$lt': datetime.utcnow()},
            'completed': False
        })
    
    @staticmethod
    def clear_all():
        """Clear all todos (useful for testing)"""
        return mongo.db.todos.delete_many({}) 