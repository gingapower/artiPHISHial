import React, { useState } from 'react';
import './App.css';
import ImageSlider from "./ImageSlider";

  

function App() {
  const [input, setInput] = useState('');
  const [message, setMessage] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);
  const slides = [
    { url: "http://localhost:3000/screenshot.png", title: "screensho1" },
    { url: "http://localhost:3000/screenshot2.png", title: "screenshot2" }
  ];
  const containerStyles = {
    width: "1000px",
    height: "500px",
    margin: "0 auto",
  };

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
        setIsSubmitted(true);
      } else {
        // Handle error response
        setMessage('Failed to submit data');
        setIsSubmitted(false);
      }
    } catch (error) {
      // Handle fetch error
      setMessage('An error occurred: ' + error.message);
      setIsSubmitted(false);
    }
  };

  return (
    <div className="container"> {/* Apply the 'container' CSS class */}
      <h1>Generate Your Phishing Page</h1>
      <div>
        <input
          type="text"
          name="link"
          placeholder="Website Link or Login Page Link"
          value={input}
          onChange={handleChange}
        />
      </div>
      <button onClick={handleSubmit}>Submit Website Link</button>
      <button onClick={handleSubmit}>Submit Login Link</button>
      {message && <p>{message}</p>}
      {isSubmitted && (
        <div>
          <h2>Thank you for submitting!</h2>
          <p>Your data has been successfully submitted.</p>
          <div style={containerStyles}>
            <ImageSlider slides={slides} />
          </div>
          {/* Additional HTML and CSS code specific to the successful response */}
        </div>
      )}
    </div>
  );
}

export default App;