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
import logo from './logo.png'
import './Home.css';
import price from './price.jpg';

const Home = () => {
  const [input, setInput] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);
  const navigate = useNavigate();

  const handleChange = (event) => {
    const inputValue = event.target.value;
    setInput(inputValue);
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
        navigate('/result?inputValue=' + input);
      } else {
        setIsSubmitted(false);
        console.log('error');
      }
    } catch (error) {
      setIsSubmitted(false);
      console.log('error');
    }
  };

  const handleAIRequestClick = () => {
    navigate('/ai_request');
  };

  return (
    <body>
      <Parallax
        pages={10}
        style={{
          backgroundImage: `url(${white})`,
          backgroundSize: '100%',
        }}
      >
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
          <div className="navbar">
            <div className="logo">
              <a href="#hero"><img src={logo} alt="Logo" /></a>
            </div>
            <div className="links">
              <ul className="nav_ul"></ul>
              <li><a href="#hero">Home</a></li>
              <li><a href="#layer2">About</a></li>
              <li><a href="#layer6">Pricing</a></li>
              <li><a href="#">Log in</a></li>
            </div>
            <div className='getstarted'>
              <button onClick={handleAIRequestClick}>Generate AI Login Page</button>
            </div>
          </div>
          {/* First page content */}
          <div id="hero" className="hero">
            <h1>Generate Your Phishing Page</h1>
            <p>
              A user-friendly web service tool that enables users to create realistic phishing pages for educational and security purposes. It simplifies the process of generating custom phishing pages, helping users enhance their understanding of phishing threats and strengthen their security measures.
            </p>
          </div>
          <div id="demo-container" className="demo-container">
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
        <ParallaxLayer offset={1.2} speed={0.3} >
          {/* Second page content */}
          <div id="layer2" className="layer2">
            <h1>Why should you create a phishing mail?</h1>
            <p>
              Training employees against phishing emails is crucial for strong cybersecurity. Phishing attacks are pervasive and can lead to data breaches, financial losses, and reputation damage. By educating employees, organizations create a vigilant workforce capable of identifying and reporting suspicious emails, thus mitigating the risk of successful phishing attempts. Empowering employees with knowledge and awareness is an essential defense against evolving cyber threats.
            </p>
          </div>
        </ParallaxLayer>

        <ParallaxLayer offset={1.989} speed={0.3} factor={1}>
          {/* Second page content */}
          <div className="layer3">
            <h1>How does it work?</h1>
            <p>
              Training employees against phishing emails is crucial for strong cybersecurity. Phishing attacks are pervasive and can lead to data breaches, financial losses, and reputation damage. By educating employees, organizations create a vigilant workforce capable of identifying and reporting suspicious emails, thus mitigating the risk of successful phishing attempts. Empowering employees with knowledge and awareness is an essential defense against evolving cyber threats.
            </p>
          </div>
        </ParallaxLayer>
        <ParallaxLayer offset={1.99} speed={0.8}>
          <div className="imagec1">
            <img src={startscreen} alt="Image 1" className="screen" />
          </div>
        </ParallaxLayer>

        <ParallaxLayer offset={2} speed={0.9}>
          <div className="imagec2">
            <img src={clonescreen} alt="Image 1" className="screen" />
          </div>
        </ParallaxLayer>
        <ParallaxLayer offset={2.2} speed={0.99}>
          {/* Second page content */}
          <div className="layer4">
            <h1>The orginal Page gets cloned</h1>
            <p>
              The website is automatically cloned and shown to you. Now you can decide if you want to download this website or if you want to generate one with AI.
            </p>
          </div>
        </ParallaxLayer>
        <ParallaxLayer offset={2.7} speed={1.3} >
          <div className="imagec3">
            <img src={downloadscreen} alt="Image 1" className="screen" />
          </div>
        </ParallaxLayer>
        <ParallaxLayer offset={2.9} speed={0.8}>
          {/* Second page content */}
          <div className="layer5">
            <h1>Download your Landing page</h1>
            <p>
              Training employees against phishing emails is crucial for strong cybersecurity. Phishing attacks are pervasive and can lead to data breaches, financial losses, and reputation damage. By educating employees, organizations create a vigilant workforce capable of identifying and reporting suspicious emails, thus mitigating the risk of successful phishing attempts. Empowering employees with knowledge and awareness is an essential defense against evolving cyber threats.
            </p>
          </div>
        </ParallaxLayer>
        <ParallaxLayer offset={3} speed={0.8} style={{
            backgroundImage: `url(${white})`,
            backgroundSize: '100%',
          }}>
        <ParallaxLayer offset={1.5} speed={1} >
        <div className="imagec4">
            <img src={price} alt="Image Price" className="priceimage" />
          </div>
        </ParallaxLayer>
          {/* Pricing page content */}
          <div id="layer6" className="layer6">
            <h1>Simple Pricing for everyone</h1>
            <p className='layer6p'>Pricing built for businesses of all sizes. Always know what you’ll pay.</p>
            <div className="pricingtable">
            <h2>
              Security Plus
            </h2>
            <h3>
              Features
            </h3>
            <p>Our tool will scrape the website you provide or generates a Login Page with AI.</p>
            <h5>$10/mo</h5>
            <button onClick={handleSubmit}>Get Started</button>
            </div>
          </div>
        </ParallaxLayer>
      </Parallax>
    </body>
  );
};

export default Home;
