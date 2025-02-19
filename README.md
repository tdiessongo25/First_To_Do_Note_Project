# Full Stack Todo Application
A modern todo application built with Flask (Backend) and React (Frontend), featuring a clean UI and robust functionality.

## Features
- ✅ Create, Read, Update, and Delete todos
- 📂 Organize todos by categories
- 🔍 Search and filter todos
- ⏰ Set due dates for tasks
- 🔄 Sort by different criteria (created date, due date, title)
- 📱 Responsive design
- ✨ Material-UI components

## Tech Stack

### Backend
- Flask
- MongoDB
- Flask-PyMongo
- Flask-CORS
- Python-dotenv

### Frontend
- React
- Material-UI
- Axios
- Date-fns
- React Router

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js
- MongoDB

### Installation
1. Clone the repository
2. Set up the backend
3. Set up the frontend
4. Start MongoDB

### Running the Application
1. Start the backend server (from project root)
2. Start the frontend development server (in another terminal)
   
The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/todos` | Get all todos |
| POST | `/api/todos` | Create a new todo |
| PUT | `/api/todos/<id>` | Update a todo |
| DELETE | `/api/todos/<id>` | Delete a todo |
| GET | `/api/categories` | Get all categories |
| GET | `/api/todos/overdue` | Get overdue todos |


## Project Structure
first_to_do_project/
├── frontend/ # React frontend
│ ├── src/
│ │ ├── components/ # React components
│ │ ├── services/ # API services
│ │ └── utils/ # Utility functions
│ └── package.json
├── todo_app/ # Flask backend
│ ├── models/ # Database models
│ ├── routes/ # API routes
│ ├── tests/ # Test files
│ ├── init.py # App initialization
│ └── config.py # Configuration
├── .env # Environment variables
├── .gitignore
├── README.md
└── run.py # App entry point

## Testing
Run backend tests

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License.
MIT License

Copyright (c) 2024 Thierry Diessongo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Acknowledgments
- Material-UI for the beautiful components
- MongoDB for the database
- Flask for the backend framework
- React for the frontend framework

# Design Patterns in Todo App

## Creational Patterns

### Factory Pattern (TodoFactory)
- **Purpose**: Creates different types of todos with specific properties
- **Use Cases**: 
  - Creating tasks with basic properties
  - Creating reminders with priority
  - Creating project todos with subtasks
- **Location**: `src/factories/TodoFactory.ts`

### Singleton Pattern (AppConfig)
- **Purpose**: Maintains a single configuration instance across the app
- **Use Cases**:
  - Managing API URLs
  - Storing app-wide settings
  - Maintaining consistent configuration
- **Location**: `src/config/AppConfig.ts`

## Behavioral Patterns

### Chain of Responsibility (TodoValidators)
- **Purpose**: Processes todo validation in a chain
- **Use Cases**:
  - Validating todo title
  - Checking due date validity
  - Extensible validation chain
- **Location**: `src/validators/TodoValidators.ts`

### Strategy Pattern (TodoFilterStrategy)
- **Purpose**: Implements different filtering algorithms
- **Use Cases**:
  - Filtering active todos
  - Filtering completed todos
  - Filtering overdue todos
- **Location**: `src/strategies/TodoFilterStrategy.ts`

## Structural Patterns

### Decorator Pattern (TodoDecorators)
- **Purpose**: Adds behavior to todo repository
- **Use Cases**:
  - Logging operations
  - Validating data
  - Adding cross-cutting concerns
- **Location**: `src/decorators/TodoDecorators.ts`

## Integration Points

All patterns are integrated in the TodoList component (`src/components/TodoList.tsx`):
- Factory creates new todos
- Validators ensure data integrity
- Strategy handles filtering
- Decorators manage repository operations
- Singleton provides configuration

## Testing

Each pattern has corresponding tests in `src/__tests__/`:
- `TodoFactory.test.ts`
- `TodoValidators.test.ts`
- `AppConfig.test.ts`
- etc.
