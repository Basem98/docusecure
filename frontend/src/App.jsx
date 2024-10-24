import { Route, Routes } from 'react-router-dom'
import './App.css'
import Home from './pages/Home'
import SearchEngine from './pages/SearchEngine'

function App() {

  return (
    <div className='app-container'>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/searchengine" element={<SearchEngine />} />
      </Routes>
    </ div>
  )
}

export default App
