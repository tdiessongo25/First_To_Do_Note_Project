import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';

function Header() {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Todo App
        </Typography>
        <Button color="inherit" component={RouterLink} to="/">
          All Todos
        </Button>
        <Button color="inherit" component={RouterLink} to="/overdue">
          Overdue
        </Button>
      </Toolbar>
    </AppBar>
  );
}

export default Header; 