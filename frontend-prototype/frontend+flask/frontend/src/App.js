import React, { useState } from 'react';

function App() {
  const [input, setInput] = useState('');

  const handleChange = (event) => {
    setInput(event.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch('/submit_data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input }),
      });

      if (response.ok) {
        // Handle successful response
        console.log('Data submitted successfully');
      } else {
        // Handle error response
        console.error('Failed to submit data');
      }
    } catch (error) {
      // Handle fetch error
      console.error('An error occurred:', error);
    }
  };

  return (
    <div>
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
    </div>
  );
}

export default App;
