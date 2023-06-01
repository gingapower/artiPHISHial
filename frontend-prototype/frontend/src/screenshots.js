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
      setMessage('worked')
    } else {
      setMessage('An error occurred');
    }
  } catch (error) {
    setMessage('An error occurred: ' + error.message);
  }
};
const download =async (event) => {
  event.preventDefault();
  // const checkbox = document.getElementById('checkbox');
  const checkbox = document.getElementById('checkbox').checked;

  try {
    const response = await fetch('http://localhost:5000/download_flask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputValue, checkbox}),
    });

    if (response.ok) {
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'flaskapp.zip'; // Replace with the desired filename and extension
      a.click();
      URL.revokeObjectURL(url);
    } else {
      setMessage('An error occurred');
    }
  } catch (error) {
    setMessage('An error occurred: ' + error.message);
  }
};
const download2 =async (event) => {
  event.preventDefault();

  try {
    const response = await fetch('http://localhost:5000/download_var', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputValue }),
    });

    if (response.ok) {
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'flaskapp.exe'; // Replace with the desired filename and extension
      a.click();
      URL.revokeObjectURL(url);
    } else {
      setMessage('An error occurred');
    }
  } catch (error) {
    setMessage('An error occurred: ' + error.message);
  }
};
const handleNavigateHome = () => {
  navigate('/');
};

const handleAIRequest = () => {
  navigate('/ai_request');
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
        <div className='askDivision'>
        <div className='tryDivision'>
          <h3>Did not like it? Try with AI or go back to Home:</h3>
        </div>
        <div className="button-container-div">
          <button className='navigateHome' onClick={handleNavigateHome}>Go to Home</button>
          <button className='navigateAI' onClick={handleAIRequest}>Try with AI</button>
        </div>
        </div>
        <div className="Button">
          {/* Input and button */}
          <button onClick={trySubmit}>Try again</button>
        </div>
        <div class="rectangle">
          <h2 class="headline">Download Executable</h2>
          <p class="text">Download .exe file which deploys the phishing mail on your local system!</p>
          <div class="checkbox-wrapper">
            <input type="checkbox" id="checkbox"></input>
            <label for="checkbox">remove scripts</label>
          </div>
          <button class="btn" onClick={download}>{message ? 'Downloading...' : 'Download'}</button>
        </div>
        <div class="rectangle2">
          <h2 class="headline">Download HTML </h2>
          <p class="text">Download just html and css files!</p>
          <button class="btn" onClick={download}>{message ? 'Downloading...' : 'Download'}</button>
        </div>
        <div class="footer"></div>
        </body>
        
      );
    }

