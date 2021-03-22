import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

import AppRoutes from './app-routes.js';
import { Container, Row, Col } from 'react-bootstrap';

function App() {
  return (
    <Container>
        <AppRoutes/>
    </Container>
  );
}

export default App;
