import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Request.css';

const Request = () => {
  const [isAIRequesting, setIsAIRequesting] = useState(false);
  const [name, setCompanyName] = useState('');
  const [domain, setDomain] = useState('');
  const [htmlContent, setHtmlContent] = useState('');
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

        const responseData = await response.json();
        const { htmlPath, cssPath } = responseData;

        setHtmlContent(`
          <link rel="stylesheet" href="${cssPath}">
          <div>${htmlPath}</div>
        `);
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

  return (
  <body>
    <div className='container'>
      <h1 className='heading'>Generate Your Login Page with OpenAI</h1>
      <input className='input-field'
        type="text"
        value={name}
        onChange={(e) => setCompanyName(e.target.value)}
        placeholder="Company Name"
      />
      <input className='input-field'
        type="text"
        value={domain}
        onChange={(e) => setDomain(e.target.value)}
        placeholder="Domain (link)"
      />
      <button className='aiButton' onClick={handleAIRequest} disabled={isAIRequesting}>
        {isAIRequesting ? 'Performing AI Request...' : 'Perform AI Request'}
      </button>
      <button className='backButton' onClick={handleNavigateHome}>Go back to Home</button>

      {htmlContent && (
        <div dangerouslySetInnerHTML={{ __html: htmlContent }}></div>
      )}
    </div>
  </body>
  );
};

export default Request;
