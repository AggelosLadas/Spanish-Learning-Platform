import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { ProgressProvider } from './context/ProgressContext';
import Navbar from './components/common/Navbar';
import HomePage from './pages/HomePage';
import ChapterListPage from './pages/ChapterListPage';
import LessonPage from './pages/LessonPage';
import ExamPage from './pages/ExamPage';
import ResultsPage from './pages/ResultsPage';
import ProgressPage from './pages/ProgressPage';

export default function App() {
  return (
    <BrowserRouter>
      <ProgressProvider>
        <div className="min-h-screen bg-background">
          <Navbar />
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/learn" element={<ChapterListPage />} />
            <Route path="/learn/:chapterId" element={<LessonPage />} />
            <Route path="/exam/:chapterId" element={<ExamPage />} />
            <Route path="/results/:chapterId" element={<ResultsPage />} />
            <Route path="/progress" element={<ProgressPage />} />
          </Routes>
        </div>
      </ProgressProvider>
    </BrowserRouter>
  );
}
