import React, { useState } from 'react';
import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [message, setMessage] = useState('');

  const handleChange = (event) => {
    setInput(event.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://localhost:5000/submit_data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input }),
      });

      if (response.ok) {
        // Handle successful response
        setMessage('Data submitted successfully');
      } else {
        // Handle error response
        setMessage('Failed to submit data');
      }
    } catch (error) {
      // Handle fetch error
      setMessage('An error occurred: ' + error.message);
    }
  };

  return (
    <div className="container"> {/* Apply the 'container' CSS class */}
      <h1>Generate Your Phishing Page</h1>
      <div>
        <input
          type="text"
          name="link"
          placeholder="Link to Website/Login Page"
          value={input}
          onChange={handleChange}
        />
      </div>
      <button onClick={handleSubmit}>Submit</button>
      {message && <p>{message}</p>}
    </div>
  );
}

export default App;
