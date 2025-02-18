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
