import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Request.css';

const Request = () => {
  const [isAIRequesting, setIsAIRequesting] = useState(false);
  const [isDownloading, setIsDownloading] = useState(false);
  const [companyName, setCompanyName] = useState(''); // Add state for the company name
  const navigate = useNavigate();

  const handleAIRequest = async () => {
    setIsAIRequesting(true);

    try {
      // Perform AI Request logic
      const response = await fetch('http://localhost:5000/ai_request', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: companyName }), // Pass the company name in the request payload
      });

      if (response.ok) {
        // AI Request success
        console.log('AI Request completed successfully');
      } else {
        // AI Request failed
        console.log('AI Request failed');
      }
    } catch (error) {
      console.log('Error occurred during AI Request:', error);
    } finally {
      setIsAIRequesting(false);
    }
  };

  const handleDownloadFiles = () => {
    setIsDownloading(true);

    try {
      // Download files logic
      console.log('Downloading files...');

      // Simulate file download delay (2 seconds)
      setTimeout(() => {
        console.log('Files downloaded successfully');
        setIsDownloading(false);
      }, 2000);
    } catch (error) {
      console.log('Error occurred during file download:', error);
      setIsDownloading(false);
    }
  };

  const handleNavigateHome = () => {
    navigate('/');
  };

  return (
    <div>
      <h1>AI Request Page</h1>
      <input
        type="text"
        value={companyName}
        onChange={(e) => setCompanyName(e.target.value)}
        placeholder="Company Name"
      /> {/* Add an input field for the company name */}
      <button onClick={handleAIRequest} disabled={isAIRequesting}>
        {isAIRequesting ? 'Performing AI Request...' : 'Perform AI Request'}
      </button>
      <button onClick={handleDownloadFiles} disabled={isDownloading}>
        {isDownloading ? 'Downloading...' : 'Download Files'}
      </button>
      <button onClick={handleNavigateHome}>Go back to Home</button>
    </div>
  );
};

export default Request;
