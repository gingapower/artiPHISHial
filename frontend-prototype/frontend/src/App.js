import React, { useState } from 'react';
import './App.css';
import { BeatLoader } from 'react-spinners';
import { Parallax, ParallaxLayer } from '@react-spring/parallax';
import background from './background.png';

function App() {
  const [input, setInput] = useState('');
  const [setMessage] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [showSuccessPage, setShowSuccessPage] = useState(false); // New state to control success page rendering

  const handleChange = (event) => {
    setInput(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      setIsSubmitted(true);

      const response = await fetch('http://localhost:5000/submit_data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input }),
      });

      if (response.ok) {
        setIsSubmitted(false);
        setShowSuccessPage(true); // Set showSuccessPage to true on successful response
      } else {
        setIsSubmitted(false);
        setMessage('Failed to submit data');
      }
    } catch (error) {
      setIsSubmitted(false);
      setMessage('An error occurred: ' + error.message);
    }
  };

  return (
    <div className={`container ${isSubmitted ? 'dark-overlay' : ''}`}>
      <nav className="top-nav">
        <div className="logo-container">
          <img src="logo.png" alt="Logo" className="logo" />
        </div>
        <ul className="facts-list">
          <li>
            <a href="#">About</a>
          </li>
          <li>
            <a href="#">Pricing</a>
          </li>
          <li>
            <a href="#">Documentation</a>
          </li>
          <li>
            <a href="#">Contact</a>
          </li>
        </ul>
      </nav>
      <Parallax pages={3}>
        <ParallaxLayer style={{
            backgroundImage: `url(${background})`,
            backgroundSize: 'cover',
          }} offset={0}
          speed={1}
          factor={2}>
        
        </ParallaxLayer>
        <ParallaxLayer speed={0.1}>
          {/* First page content */}
          <div className="hero">
            <h1>Generate Your Phishing Page</h1>
            <p>A user-friendly web service tool that enables users to create realistic phishing pages for educational and security purposes. It simplifies the process of generating custom phishing pages, helping users enhance their understanding of phishing threats and strengthen their security measures.</p>
          </div>
          <div className="demo-container">
            {/* Input and button */}
          
                <input
                  type="text"
                  name="link"
                  placeholder="Website Link or Login Page Link"
                  value={input}
                  onChange={handleChange}
                />
                <button onClick={handleSubmit}>Submit Website Link</button>
                <button onClick={handleSubmit}>Submit Login Link</button>
            
            {isSubmitted && (
              <div className="loader-container">
                <BeatLoader color="#384E77" loading={true} />
                <p>Loading...</p>
              </div>
            )}
          </div>
        </ParallaxLayer>
        <ParallaxLayer offset={1} speed={1}>
          {/* Second page content */}
          <div className="hero">
            <h1>Generate Your Phishing Page</h1>
            <p>A user-friendly web service tool that enables users to create realistic phishing pages for educational and security purposes. It simplifies the process of generating custom phishing pages, helping users enhance their understanding of phishing threats and strengthen their security measures.</p>
          </div>
        </ParallaxLayer>
      </Parallax>   
    </div>
  );
  
}
export default App;