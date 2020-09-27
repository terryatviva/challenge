import React from 'react';
import './App.css';
import Index from './Components/Index'
import List from './Components/List'
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import {Navbar} from "react-bootstrap";
import logo from "./Components/logo.png";


function App() {
  return (
    <Router>
           <div>
               <Navbar bg="dark" style = {{height: 80}}>
            <Navbar.Brand>
                <img
                src={logo}
                width="200"
                height="100"
                className="d-inline-block align-top"
                alt="React Bootstrap logo"
                />
            </Navbar.Brand>
        </Navbar>
            <Route exact path='/' component={Index}></Route>
            <Route exact path='/List' component={List}></Route>

           </div>
    </Router>
  );
}

export default App;
