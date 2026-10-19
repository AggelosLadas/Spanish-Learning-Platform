import { useEffect, useState, useCallback } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import Button from '../components/common/Button';
import SectionRenderer from '../components/lesson/SectionRenderer';
import { fetchChapter, fetchChapterSections } from '../services/api';
import { useProgress } from '../context/ProgressContext';

const sectionTypeIcons = {
  text: '📄',
  vocab: '📖',
  grammar: '📐',
  example: '💬',
  tip: '💡',
  video: '▶️',
};

export default function LessonPage() {
  const { chapterId } = useParams();
  const navigate = useNavigate();
  const { markSectionViewed, getSectionsViewed, updateProgress } = useProgress();

  const [chapter, setChapter] = useState(null);
  const [sections, setSections] = useState([]);
  const [currentIdx, setCurrentIdx] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const viewedIds = getSectionsViewed(Number(chapterId));

  useEffect(() => {
    setLoading(true);
    setError(null);
    Promise.all([
      fetchChapter(chapterId),
      fetchChapterSections(chapterId),
    ])
      .then(([ch, secs]) => {
        setChapter(ch);
        setSections(secs);
        setLoading(false);
      })
      .catch(() => {
        setError('Σφάλμα κατά τη φόρτωση του μαθήματος.');
        setLoading(false);
      });
  }, [chapterId]);

  const currentSection = sections[currentIdx];
  const totalSections = sections.length;
  const isFirst = currentIdx === 0;
  const isLast = currentIdx === totalSections - 1;

  const markCurrentViewed = useCallback(() => {
    if (!currentSection) return;
    markSectionViewed(Number(chapterId), currentSection.id);

    const allIds = sections.map(s => s.id);
    const newViewed = [...new Set([...viewedIds, currentSection.id])];
    const allViewed = allIds.every(id => newViewed.includes(id));
    if (allViewed) {
      updateProgress(Number(chapterId), { lessonViewed: true });
    }
  }, [currentSection, chapterId, sections, viewedIds, markSectionViewed, updateProgress]);

  useEffect(() => {
    markCurrentViewed();
  }, [markCurrentViewed]);

  const goToSection = (idx) => {
    setCurrentIdx(idx);
    setSidebarOpen(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const goNext = () => {
    if (!isLast) goToSection(currentIdx + 1);
  };

  const goPrev = () => {
    if (!isFirst) goToSection(currentIdx - 1);
  };

  useEffect(() => {
    const handleKey = (e) => {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        e.preventDefault();
        goNext();
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault();
        goPrev();
      }
    };
    window.addEventListener('keydown', handleKey);
    return () => window.removeEventListener('keydown', handleKey);
  });

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="text-center">
          <div className="animate-spin w-12 h-12 border-4 border-primary border-t-transparent rounded-full mx-auto mb-4" />
          <p className="text-secondary/60">Φόρτωση μαθήματος...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16 text-center">
        <div className="text-5xl mb-4">⚠️</div>
        <p className="text-lg text-error mb-4">{error}</p>
        <Link to="/learn">
          <Button variant="outline">← Πίσω στα Κεφάλαια</Button>
        </Link>
      </div>
    );
  }

  const viewedCount = sections.filter(s => viewedIds.includes(s.id)).length;
  const allViewed = viewedCount === totalSections;

  return (
    <div className="min-h-[calc(100vh-4rem)] flex flex-col lg:flex-row">
      {/* Mobile sidebar toggle */}
      <button
        onClick={() => setSidebarOpen(!sidebarOpen)}
        className="lg:hidden fixed bottom-4 left-4 z-40 bg-secondary text-white p-3 rounded-full shadow-lg hover:bg-secondary-light transition-colors"
        aria-label="Εμφάνιση ενοτήτων"
      >
        <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>

      {/* Sidebar overlay (mobile) */}
      {sidebarOpen && (
        <div className="lg:hidden fixed inset-0 bg-black/40 z-30" onClick={() => setSidebarOpen(false)} />
      )}

      {/* Sidebar */}
      <aside
        className={`fixed lg:sticky top-16 left-0 z-30 h-[calc(100vh-4rem)] w-72 bg-white border-r border-neutral/20 
          overflow-y-auto transition-transform duration-300 lg:translate-x-0 flex-shrink-0
          ${sidebarOpen ? 'translate-x-0' : '-translate-x-full'}`}
      >
        <div className="p-4">
          {/* Chapter header */}
          <Link to="/learn" className="flex items-center gap-2 text-sm text-secondary/60 hover:text-primary mb-4 transition-colors">
            ← Πίσω στα Κεφάλαια
          </Link>
          <h3 className="font-bold text-secondary text-sm mb-1">
            Κεφάλαιο {chapter.order_index}
          </h3>
          <h2 className="font-extrabold text-secondary text-lg mb-1">
            {chapter.title_greek}
          </h2>
          <p className="text-sm text-secondary/50 italic mb-4">{chapter.title_spanish}</p>

          {/* Progress */}
          <div className="mb-4">
            <div className="flex justify-between text-xs text-secondary/60 mb-1">
              <span>Πρόοδος</span>
              <span>{viewedCount}/{totalSections}</span>
            </div>
            <div className="w-full bg-neutral/30 rounded-full h-2">
              <div
                className="h-2 bg-gradient-to-r from-primary to-success rounded-full transition-all duration-500"
                style={{ width: `${totalSections > 0 ? (viewedCount / totalSections) * 100 : 0}%` }}
              />
            </div>
          </div>

          {/* Section list */}
          <nav className="space-y-1">
            {sections.map((sec, idx) => {
              const isViewed = viewedIds.includes(sec.id);
              const isCurrent = idx === currentIdx;
              return (
                <button
                  key={sec.id}
                  onClick={() => goToSection(idx)}
                  className={`w-full text-left flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm transition-all
                    ${isCurrent
                      ? 'bg-primary/10 text-primary font-semibold border border-primary/20'
                      : isViewed
                        ? 'text-success hover:bg-success/5'
                        : 'text-secondary/70 hover:bg-secondary/5'
                    }`}
                >
                  <span className={`flex-shrink-0 w-6 h-6 rounded-full flex items-center justify-center text-xs border
                    ${isCurrent ? 'bg-primary text-white border-primary' : isViewed ? 'bg-success/20 text-success border-success/30' : 'bg-secondary/10 text-secondary/50 border-secondary/20'}`}>
                    {isViewed && !isCurrent ? '✓' : idx + 1}
                  </span>
                  <span className="truncate flex-1">
                    {sectionTypeIcons[sec.type] || '📄'}{' '}
                    {sec.content_json?.title || `Ενότητα ${idx + 1}`}
                  </span>
                </button>
              );
            })}
          </nav>
        </div>
      </aside>

      {/* Main content */}
      <main className="flex-1 min-w-0">
        {/* Top bar */}
        <div className="sticky top-16 z-10 bg-background/95 backdrop-blur border-b border-neutral/20 px-4 lg:px-8 py-3">
          <div className="max-w-3xl mx-auto flex items-center justify-between">
            <div className="text-sm text-secondary/60">
              <span className="font-semibold text-secondary">Κεφάλαιο {chapter.order_index}</span>
              {' · '}
              Ενότητα {currentIdx + 1} από {totalSections}
            </div>
            <div className="flex items-center gap-1.5">
              {sections.map((sec, idx) => (
                <button
                  key={sec.id}
                  onClick={() => goToSection(idx)}
                  className={`w-2.5 h-2.5 rounded-full transition-all ${
                    idx === currentIdx
                      ? 'bg-primary scale-125'
                      : viewedIds.includes(sec.id)
                        ? 'bg-success'
                        : 'bg-secondary/20'
                  }`}
                  aria-label={`Ενότητα ${idx + 1}`}
                />
              ))}
            </div>
          </div>
        </div>

        {/* Section content */}
        <div className="max-w-3xl mx-auto px-4 lg:px-8 py-8">
          {currentSection && (
            <div className="animate-fadeIn">
              <SectionRenderer section={currentSection} />
            </div>
          )}
        </div>

        {/* Bottom navigation */}
        <div className="sticky bottom-0 bg-white/95 backdrop-blur border-t border-neutral/20 px-4 lg:px-8 py-4">
          <div className="max-w-3xl mx-auto flex items-center justify-between">
            <Button
              variant="ghost"
              size="sm"
              onClick={goPrev}
              disabled={isFirst}
            >
              ← Προηγούμενο
            </Button>

            <span className="text-sm text-secondary/50 hidden sm:inline">
              {viewedCount}/{totalSections} ενότητες
            </span>

            {isLast ? (
              allViewed ? (
                <Button
                  variant="success"
                  size="sm"
                  onClick={() => navigate(`/exam/${chapterId}`)}
                >
                  Πάμε στην Εξέταση! →
                </Button>
              ) : (
                <Button variant="outline" size="sm" disabled>
                  Ολοκλήρωσε όλες τις ενότητες
                </Button>
              )
            ) : (
              <Button
                variant="primary"
                size="sm"
                onClick={goNext}
              >
                Επόμενο →
              </Button>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}
