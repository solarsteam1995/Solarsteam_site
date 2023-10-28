import React from 'react';
import './App.css';
import HamburgerMenu from './HamburgerMenu';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <HamburgerMenu />
        <h1>Welcome to My Landing Page</h1>
        <p>This is a simple landing page created with React.</p>
      </header>
    </div>
  );
}

export default App;
