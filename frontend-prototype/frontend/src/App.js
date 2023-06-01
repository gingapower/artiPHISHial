import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './Home'
import Result from './screenshots'
import AIRequest from './AIRequest'


function App() {
   return (
    <>
      <BrowserRouter>
        <Routes>
        <Route index element={<Home />} />
        <Route path='result' element={<Result />} />
        <Route path='ai_request' element={<AIRequest />} />
        </Routes>
      </BrowserRouter>
    </>
    
  );
  
}
export default App;