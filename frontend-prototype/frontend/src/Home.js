import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { BeatLoader } from 'react-spinners';
import { Parallax, ParallaxLayer } from '@react-spring/parallax';
import background from './bg.png';
import background1 from './bg3.png';
import startscreen from './startscreen.png'
import clonescreen from './clonescreen.png'
import downloadscreen from './downloadscreen.png'
import white from './white.png'
import './Home.css';

export default function Home(){
  const [input, setInput] = useState('');
  const [setMessage] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);
  const navigate = useNavigate()

  const handleChange = (event) => {
    setInput(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      setIsSubmitted(true);

      const response = await fetch('http://localhost:5000/submit_data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input }),
      });

      if (response.ok) {
        setIsSubmitted(false);
        navigate('result');
      } else {
        setIsSubmitted(false);
        setMessage('Failed to submit data');
      }
    } catch (error) {
      setIsSubmitted(false);
      setMessage('An error occurred: ' + error.message);
    }
  };
  return (
    <body>
      <Parallax pages={9}>
        <ParallaxLayer
          style={{
            backgroundImage: `url(${background})`,
            backgroundSize: '100%',
          }}
          offset={0}
          speed={0.5}
          factor={2}
        ></ParallaxLayer>
        <ParallaxLayer speed={0.1} factor={10}>
          {/* First page content */}
          <div className="hero">
            <h1>Generate Your Phishing Page</h1>
            <p>
              A user-friendly web service tool that enables users to create realistic phishing pages for educational and security purposes. It simplifies the process of generating custom phishing pages, helping users enhance their understanding of phishing threats and strengthen their security measures.
            </p>
          </div>
          <div className="demo-container">
            {/* Input and button */}
            <input type="text" name="link" placeholder="Website Link or Login Page Link" value={input} onChange={handleChange} />
            <button onClick={handleSubmit}>Submit Website Link</button>
            <button onClick={() => navigate('result')}>Submit Login Link</button>
            {isSubmitted && (
              <div className="loader-container">
                <BeatLoader color="#384E77" loading={true} />
                <p>Loading...</p>
              </div>
            )}
          </div>
        </ParallaxLayer>
        <ParallaxLayer
          style={{
            backgroundImage: `url(${background1})`,
            backgroundSize: '100%',
          }}
          offset={1}
          speed={0.5}
          factor={2}
        ></ParallaxLayer>
        <ParallaxLayer offset={1} speed={2} >
          {/* Second page content */}
          <div className="layer2">
            <h1>Why should you create a phishing mail?</h1>
            <p>
            Training employees against phishing emails is crucial for strong cybersecurity. Phishing attacks are pervasive and can lead to data breaches, financial losses, and reputation damage. By educating employees, organizations create a vigilant workforce capable of identifying and reporting suspicious emails, thus mitigating the risk of successful phishing attempts. Empowering employees with knowledge and awareness is an essential defense against evolving cyber threats.
            </p>
          </div>
        </ParallaxLayer>
        
        <ParallaxLayer offset={1.9} speed={0.4} factor={1}>
          {/* Second page content */}
          <div className="layer3">
            <h1>How does it work?</h1>
            <p>
            Training employees against phishing emails is crucial for strong cybersecurity. Phishing attacks are pervasive and can lead to data breaches, financial losses, and reputation damage. By educating employees, organizations create a vigilant workforce capable of identifying and reporting suspicious emails, thus mitigating the risk of successful phishing attempts. Empowering employees with knowledge and awareness is an essential defense against evolving cyber threats.
            </p>
          </div>
        </ParallaxLayer>
        <ParallaxLayer offset={1.99} speed={0.8}>
          <div className='imagec1'>
            <img src={startscreen} alt="Image 1" className="screen" />
          </div>
        </ParallaxLayer>
        
        <ParallaxLayer offset={2} speed={0.9} >
          <div className='imagec2'>
            <img src={clonescreen} alt="Image 1" className="screen" />
          </div>
        </ParallaxLayer>
        <ParallaxLayer offset={2.1} speed={0.99} >
          {/* Second page content */}
          <div className="layer4">
            <h1>The orginal Page gets cloned</h1>
            <p>
              The website is automaticly cloned and shown to you. Now you can decide if you wnat to download this website, or if you want to generate one with AI.
            </p>
          </div>
        </ParallaxLayer>
        <ParallaxLayer offset={2.7} speed={1.3} >
          <div className='imagec3'>
            <img src={downloadscreen} alt="Image 1" className="screen" />
          </div>
        </ParallaxLayer>
        <ParallaxLayer offset={2.8} speed={0.8}   >
          {/* Second page content */}
          <div className="layer5">
            <h1>Download your Landing page</h1>
            <p>
            Training employees against phishing emails is crucial for strong cybersecurity. Phishing attacks are pervasive and can lead to data breaches, financial losses, and reputation damage. By educating employees, organizations create a vigilant workforce capable of identifying and reporting suspicious emails, thus mitigating the risk of successful phishing attempts. Empowering employees with knowledge and awareness is an essential defense against evolving cyber threats.
            </p>
          </div>
        </ParallaxLayer>
      </Parallax>
    </body>
    
    
  );
  
}
// export default App;