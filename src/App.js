import React from 'react';
import './App.css';
import HamburgerMenu from './HamburgerMenu';

function App() {
  return (
    <div className="App">
      <header className="section1">
        <HamburgerMenu />
        {/* <h1>Welcome to My Landing Page</h1> */}
      </header>
      
      <section className="section2">
        <h2>New Content Here</h2>
        <p>This is some additional content that appears as you scroll.</p>
      </section>
    </div>
  );
}

export default App;
