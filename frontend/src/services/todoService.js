import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const todoService = {
    async getAllTodos() {
        const response = await axios.get(`${API_URL}/todos`);
        return response.data;
    },

    async createTodo(todo) {
        const response = await axios.post(`${API_URL}/todos`, todo);
        return response.data;
    },

    async updateTodo(id, updates) {
        const response = await axios.put(`${API_URL}/todos/${id}`, updates);
        return response.data;
    },

    async deleteTodo(id) {
        const response = await axios.delete(`${API_URL}/todos/${id}`);
        return response.data;
    },

    async getCategories() {
        const response = await axios.get(`${API_URL}/categories`);
        return response.data;
    },

    async getOverdueTodos() {
        const response = await axios.get(`${API_URL}/todos/overdue`);
        return response.data;
    }
}; 