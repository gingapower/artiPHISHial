import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Request.css';

export default function Response() {
  const [isAIRequesting, setIsAIRequesting] = useState(false);
  const [name, setCompanyName] = useState('');
  const [domain, setDomain] = useState('');
  const [isDownload, setIsDownload] = useState(false);
  const navigate = useNavigate();

  const handleAIRequest = async () => {
    setIsAIRequesting(true);

    try {
      const response = await fetch('http://localhost:5000/ai_request', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ domain, name }),
      });

      if (response.ok) {
        console.log('AI Request completed successfully');
      } else {
        console.log('AI Request failed');
      }
    } catch (error) {
      console.log('Error occurred during AI Request:', error);
    } finally {
      setIsAIRequesting(false);
    }
  };

  const handleNavigateHome = () => {
    navigate('/');
  };

  const handleDownload = async () => {
    setIsDownload(true);
    try {
      const response = await fetch('http://localhost:5000/download_ai', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        }
      });

      if (response.ok) {
        const blob = await response.blob();
        const downloadUrl = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = downloadUrl;
        link.download = 'ai_loginpage.zip';
        link.click();
        console.log('Download completed successfully');
      } else {
        console.log('Download failed');
      }
    } catch (error) {
      console.log('Error occurred during download:', error);
    } finally {
      setIsDownload(false);
    }
  };

  return (
    <body  className='body'>
      <div>
        <div className='ai-container'>
          <h1 className='heading'>Generate Your Login Page with OpenAI</h1>
          <input
            className='input-field'
            type="text"
            value={name}
            onChange={(e) => setCompanyName(e.target.value)}
            placeholder="Company Name"
          />
          <input
            className='input-field'
            type="text"
            value={domain}
            onChange={(e) => setDomain(e.target.value)}
            placeholder="Domain (Website link)"
          />
          <div className="button-container">
            <button className='aiButton' onClick={handleAIRequest} disabled={isAIRequesting}>
              {isAIRequesting ? 'Performing AI Request...' : 'Perform AI Request'}
            </button>
            <button className='backButton' onClick={handleNavigateHome}>Go back to Home</button>
          </div>
          <div className='download-container'>
          <div className='tryDiv'>
            <h3>When the Request is done download here:</h3>
          </div>
            <button className="btn" onClick={handleDownload} disabled={isDownload}>
                {isDownload ? 'Downloading...' : 'Download'}
            </button>
          </div>
        </div>
      </div>
    </body>
  );  
};