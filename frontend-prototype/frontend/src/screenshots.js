import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import './screenshot.css'
import screenshot1 from './screenshots/screenshot.png';
import screenshot2 from './screenshots/screenshot2.png';

export default function Response() {
const [setMessage] = useState('');
const { input } = useParams();

const trySubmit = async (event) => {
  event.preventDefault();

  try {
      const response = await fetch('http://localhost:5000/submit_data2', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input }),
    });

    if (response.ok) {
      setMessage('worked')
      
    } else {
      setMessage('An error occurred: ')
    }
  } catch (error) {
    setMessage('An error occurred: ' + error.message);
  }
};
    return (
      <body>
        <div className="gallery">
          <div className="image-container">
            <p>Original Page {input}</p>
            <img src={screenshot1} alt="Image 1" className="image" />
          </div>
          <p>cloned Page</p>
          <div className="image-container">
            <img src={screenshot2} alt="Image 2" className="image" />
          </div>
        </div>
        <div className="Button">
          {/* Input and button */}
          <button onClick={trySubmit}>Try again (second try)</button>
        </div>
        
        </body>
        
      );
    }

