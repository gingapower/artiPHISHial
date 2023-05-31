import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './Home'
import Result from './screenshots'
import download from './download';
import Test from './test'


function App() {
   return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
          <Route path='result' element={<Result />}/>
          <Route path='download' elemet={<download />}/>
          <Route path='test' elemet={<Test />}/>
        </Routes>
      </BrowserRouter>
    </>
    
  );
  
}
export default App;