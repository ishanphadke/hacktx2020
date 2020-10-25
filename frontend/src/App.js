import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState({ hits: [] });



  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/users">Users</Link>
            </li>
          </ul>
        </nav>

        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/users">
            <Users />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}
function Home() {
  return(
    <div>
      <h2>Home</h2>
      <button type="button" onClick = {() => testPullData}>Click Me!</button>
      <h3>{data}</h3>
    </div>
  ) 
}

function About() {
  const [count, setCount] = useState(0);


  return (
    <div>
      <h2>{count}</h2>
      <button onClick = {() => setCount(count + 1)}> 
        Click
      </button>
    </div>
    
  );
}

function Users() {
  return <h2>Users</h2>;
}

function testPullData() {
  useEffect(() => {
    fetch("/business")
        .then((res) => {
        setData(res.data)
    })
}, [ "/business" ])
}

export default App;
