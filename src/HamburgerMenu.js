import React, { useState } from 'react';
import './HamburgerMenu.css';

const HamburgerMenu = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div>
      <button className="hamburger-button" onClick={() => setIsOpen(!isOpen)}>
        ☰
      </button>
      {isOpen && (
        <nav className="hamburger-nav">
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Projects</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </nav>
      )}
    </div>
  );
};

export default HamburgerMenu;
