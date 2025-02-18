import React, { useState, useEffect } from 'react';
import {
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  IconButton,
  Checkbox,
  Paper,
  TextField,
  Button,
  Box,
  Chip,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Grid,
  Typography,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
} from '@mui/material';
import { Delete as DeleteIcon, Edit as EditIcon, Sort as SortIcon } from '@mui/icons-material';
import { todoService } from '../services/todoService';
import { format } from 'date-fns';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { LocalizationProvider, DateTimePicker } from '@mui/x-date-pickers';

function TodoList() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [filterStatus, setFilterStatus] = useState('all');
  const [sortBy, setSortBy] = useState('created');
  const [searchQuery, setSearchQuery] = useState('');
  const [editingTodo, setEditingTodo] = useState(null);
  const [dueDate, setDueDate] = useState(null);

  useEffect(() => {
    loadTodos();
    loadCategories();
  }, []);

  const loadTodos = async () => {
    try {
      const data = await todoService.getAllTodos();
      setTodos(data);
    } catch (error) {
      console.error('Error loading todos:', error);
    }
  };

  const loadCategories = async () => {
    try {
      const data = await todoService.getCategories();
      setCategories(data);
    } catch (error) {
      console.error('Error loading categories:', error);
    }
  };

  const handleAddTodo = async (e) => {
    e.preventDefault();
    if (!newTodo.trim()) return;

    try {
      await todoService.createTodo({
        title: newTodo,
        category: selectedCategory,
        due_date: dueDate,
      });
      setNewTodo('');
      setSelectedCategory('');
      setDueDate(null);
      loadTodos();
    } catch (error) {
      console.error('Error adding todo:', error);
    }
  };

  const handleEditTodo = async () => {
    if (!editingTodo) return;

    try {
      await todoService.updateTodo(editingTodo.id, {
        title: editingTodo.title,
        category: editingTodo.category,
        due_date: editingTodo.due_date,
      });
      setEditingTodo(null);
      loadTodos();
    } catch (error) {
      console.error('Error updating todo:', error);
    }
  };

  const handleToggleTodo = async (id, completed) => {
    try {
      await todoService.updateTodo(id, { completed: !completed });
      loadTodos();
    } catch (error) {
      console.error('Error toggling todo:', error);
    }
  };

  const handleDeleteTodo = async (id) => {
    if (window.confirm('Are you sure you want to delete this todo?')) {
      try {
        await todoService.deleteTodo(id);
        loadTodos();
      } catch (error) {
        console.error('Error deleting todo:', error);
      }
    }
  };

  const filteredAndSortedTodos = () => {
    let filtered = [...todos];

    // Apply search filter
    if (searchQuery) {
      filtered = filtered.filter(todo =>
        todo.title.toLowerCase().includes(searchQuery.toLowerCase())
      );
    }

    // Apply status filter
    if (filterStatus !== 'all') {
      filtered = filtered.filter(todo =>
        filterStatus === 'completed' ? todo.completed : !todo.completed
      );
    }

    // Apply category filter
    if (selectedCategory) {
      filtered = filtered.filter(todo => todo.category === selectedCategory);
    }

    // Apply sorting
    filtered.sort((a, b) => {
      switch (sortBy) {
        case 'title':
          return a.title.localeCompare(b.title);
        case 'dueDate':
          return new Date(a.due_date || '9999') - new Date(b.due_date || '9999');
        case 'created':
          return new Date(b.created_at) - new Date(a.created_at);
        default:
          return 0;
      }
    });

    return filtered;
  };

  return (
    <Box sx={{ mt: 2 }}>
      {/* Add Todo Form */}
      <Paper sx={{ p: 2, mb: 2 }}>
        <form onSubmit={handleAddTodo}>
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <TextField
                fullWidth
                value={newTodo}
                onChange={(e) => setNewTodo(e.target.value)}
                placeholder="Add a new todo"
                variant="outlined"
                size="small"
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
                <DateTimePicker
                  label="Due Date"
                  value={dueDate}
                  onChange={setDueDate}
                  renderInput={(params) => <TextField {...params} fullWidth size="small" />}
                />
              </LocalizationProvider>
            </Grid>
            <Grid item xs={12}>
              <Box sx={{ mb: 2 }}>
                {categories.map((category) => (
                  <Chip
                    key={category}
                    label={category}
                    onClick={() => setSelectedCategory(category)}
                    onDelete={selectedCategory === category ? () => setSelectedCategory('') : undefined}
                    color={selectedCategory === category ? 'primary' : 'default'}
                    sx={{ mr: 1, mb: 1 }}
                  />
                ))}
              </Box>
            </Grid>
            <Grid item xs={12}>
              <Button type="submit" variant="contained" color="primary">
                Add Todo
              </Button>
            </Grid>
          </Grid>
        </form>
      </Paper>

      {/* Filters and Search */}
      <Paper sx={{ p: 2, mb: 2 }}>
        <Grid container spacing={2} alignItems="center">
          <Grid item xs={12} sm={4}>
            <TextField
              fullWidth
              size="small"
              label="Search"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </Grid>
          <Grid item xs={12} sm={4}>
            <FormControl fullWidth size="small">
              <InputLabel>Status</InputLabel>
              <Select
                value={filterStatus}
                onChange={(e) => setFilterStatus(e.target.value)}
                label="Status"
              >
                <MenuItem value="all">All</MenuItem>
                <MenuItem value="active">Active</MenuItem>
                <MenuItem value="completed">Completed</MenuItem>
              </Select>
            </FormControl>
          </Grid>
          <Grid item xs={12} sm={4}>
            <FormControl fullWidth size="small">
              <InputLabel>Sort By</InputLabel>
              <Select
                value={sortBy}
                onChange={(e) => setSortBy(e.target.value)}
                label="Sort By"
              >
                <MenuItem value="created">Created Date</MenuItem>
                <MenuItem value="dueDate">Due Date</MenuItem>
                <MenuItem value="title">Title</MenuItem>
              </Select>
            </FormControl>
          </Grid>
        </Grid>
      </Paper>

      {/* Todo List */}
      <Paper>
        <List>
          {filteredAndSortedTodos().map((todo) => (
            <ListItem
              key={todo.id}
              divider
              sx={{
                bgcolor: todo.completed ? 'action.hover' : 'inherit',
                textDecoration: todo.completed ? 'line-through' : 'none',
              }}
            >
              <Checkbox
                checked={todo.completed}
                onChange={() => handleToggleTodo(todo.id, todo.completed)}
              />
              <ListItemText
                primary={todo.title}
                secondary={
                  <Box>
                    {todo.category && (
                      <Chip
                        label={todo.category}
                        size="small"
                        sx={{ mr: 1, mb: 1 }}
                      />
                    )}
                    {todo.due_date && (
                      <Typography variant="caption" display="block">
                        Due: {format(new Date(todo.due_date), 'PPP p')}
                      </Typography>
                    )}
                  </Box>
                }
              />
              <ListItemSecondaryAction>
                <IconButton
                  edge="end"
                  aria-label="edit"
                  onClick={() => setEditingTodo(todo)}
                  sx={{ mr: 1 }}
                >
                  <EditIcon />
                </IconButton>
                <IconButton
                  edge="end"
                  aria-label="delete"
                  onClick={() => handleDeleteTodo(todo.id)}
                >
                  <DeleteIcon />
                </IconButton>
              </ListItemSecondaryAction>
            </ListItem>
          ))}
        </List>
      </Paper>

      {/* Edit Todo Dialog */}
      <Dialog open={!!editingTodo} onClose={() => setEditingTodo(null)}>
        <DialogTitle>Edit Todo</DialogTitle>
        <DialogContent>
          <Box sx={{ pt: 2 }}>
            <TextField
              fullWidth
              label="Title"
              value={editingTodo?.title || ''}
              onChange={(e) => setEditingTodo({ ...editingTodo, title: e.target.value })}
              sx={{ mb: 2 }}
            />
            <FormControl fullWidth sx={{ mb: 2 }}>
              <InputLabel>Category</InputLabel>
              <Select
                value={editingTodo?.category || ''}
                onChange={(e) => setEditingTodo({ ...editingTodo, category: e.target.value })}
                label="Category"
              >
                {categories.map((category) => (
                  <MenuItem key={category} value={category}>
                    {category}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
            <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DateTimePicker
                label="Due Date"
                value={editingTodo?.due_date ? new Date(editingTodo.due_date) : null}
                onChange={(date) => setEditingTodo({ ...editingTodo, due_date: date })}
                renderInput={(params) => <TextField {...params} fullWidth />}
              />
            </LocalizationProvider>
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setEditingTodo(null)}>Cancel</Button>
          <Button onClick={handleEditTodo} variant="contained" color="primary">
            Save
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}

export default TodoList; 