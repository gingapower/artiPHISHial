import React, { useState } from 'react';
import { useLocation,useNavigate } from 'react-router-dom';


import './screenshot.css'
import screenshot1 from './screenshots/screenshot.png';
import screenshot2 from './screenshots/screenshot2.png';

export default function Response() {
const [message, setMessage] = useState('');
// const { inputValue } = useParams();
const location = useLocation();
const navigate = useNavigate();

// Retrieve the query parameter value
const inputValue = new URLSearchParams(location.search).get('inputValue');
// const Flask_file = "http://localhost:3000/"

const trySubmit = async (event) => {
  event.preventDefault();

  try {
    const response = await fetch('http://localhost:5000/submit_data2', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputValue }),
    });

    if (response.ok) {
      setMessage('worked');
    } else {
      setMessage('An error occurred');
    }
  } catch (error) {
    setMessage('An error occurred: ' + error.message);
  }
};
const download =async (event) => {
  event.preventDefault();

  try {
    const response = await fetch('http://localhost:5000/download_flask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputValue }),
    });

    if (response.ok) {
      setMessage('worked');
    } else {
      setMessage('An error occurred');
    }
  } catch (error) {
    setMessage('An error occurred: ' + error.message);
  }
};
const test = () => {
  navigate('/test');
};

    return (
      <body>
        <div className="gallery">
          <div className="image-container">
            <p>Original Page</p>
            <img src={screenshot1} alt="Image 1" className="image" />
          </div>
          
          <div className="image-container">
            <p>Cloned Page</p>
            <img src={screenshot2} alt="Image 2" className="image" />
          </div>
        </div>
        <div className="Button">
          {/* Input and button */}
          <button onClick={trySubmit}>Try again</button>
          <button onClick={test}>test webpae</button>
          <button onClick={download}>Download Flask</button>
        </div>
        
        </body>
        
      );
    }

