import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './Home'
import Result from './screenshots'


function App() {
   return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
          <Route path='result' element={<Result />}/>
        </Routes>
      </BrowserRouter>
    </>
    
  );
  
}
export default App;