import React from 'react';
import ImageSlider from './ImageSlider';

function ImageSliderPage({ slides }) {
    const slides = [
        { url: "http://localhost:3000/screenshot.png", title: "screensho1" },
        { url: "http://localhost:3000/screenshot2.png", title: "screenshot2" }
      ];
  const containerStyles = {
    width: '1000px',
    height: '500px',
    margin: '0 auto',
  };

  return (
    <div>
      <h2>Thank you for submitting!</h2>
      <p>Your data has been successfully submitted.</p>
      <div style={containerStyles}>
        <ImageSlider slides={slides} />
      </div>
      {/* Additional HTML and CSS code specific to the successful response */}
    </div>
  );
}

export default ImageSliderPage;
