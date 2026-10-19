import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import ProgressBar from '../components/common/ProgressBar';
import { fetchChapters } from '../services/api';
import { useProgress } from '../context/ProgressContext';

const difficultyLabels = {
  beginner: { label: 'Αρχάριος', color: 'bg-success/20 text-success', emoji: '🌱' },
  elementary: { label: 'Βασικός', color: 'bg-amber-100 text-amber-700', emoji: '📗' },
  intermediate: { label: 'Μέσος', color: 'bg-primary/20 text-primary', emoji: '🚀' },
};

const levelHeaders = {
  beginner: { title: 'Αρχάριο Επίπεδο', subtitle: 'Κεφάλαια 1-5 · Βασικές γνώσεις', color: 'from-success/10 to-success/5 border-success/20' },
  elementary: { title: 'Βασικό Επίπεδο', subtitle: 'Κεφάλαια 6-10 · Ρήματα και καθημερινότητα', color: 'from-amber-50 to-amber-50/50 border-amber-200' },
  intermediate: { title: 'Μέσο Επίπεδο', subtitle: 'Κεφάλαια 11-15 · Ανώμαλα ρήματα και παρελθόν', color: 'from-primary/5 to-primary/10 border-primary/20' },
};

const statusConfig = {
  locked: { label: 'Κλειδωμένο', icon: '🔒', color: 'text-secondary/40' },
  not_started: { label: 'Δεν ξεκίνησε', icon: '○', color: 'text-secondary/60' },
  in_progress: { label: 'Σε εξέλιξη', icon: '◐', color: 'text-amber-600' },
  completed: { label: 'Ολοκληρώθηκε', icon: '✓', color: 'text-success' },
};

function getChapterStatus(chapterProgress, isUnlocked) {
  if (!isUnlocked) return 'locked';
  if (chapterProgress.examPassed) return 'completed';
  if (chapterProgress.lessonViewed || chapterProgress.lastScore !== null) return 'in_progress';
  return 'not_started';
}

export default function ChapterListPage() {
  const [chapters, setChapters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { getChapterProgress, progress } = useProgress();

  useEffect(() => {
    fetchChapters()
      .then((data) => { setChapters(data); setLoading(false); })
      .catch(() => { setError('Σφάλμα κατά τη φόρτωση των κεφαλαίων. Δοκιμάστε ξανά.'); setLoading(false); });
  }, []);

  const isChapterUnlocked = (chapter) => {
    if (chapter.order_index === 1) return true;
    const prevChapter = chapters.find(c => c.order_index === chapter.order_index - 1);
    if (!prevChapter) return true;
    const prev = getChapterProgress(prevChapter.id);
    return prev.examPassed;
  };

  const completedCount = Object.values(progress).filter(p => p.examPassed).length;

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="text-center">
          <div className="animate-spin w-12 h-12 border-4 border-primary border-t-transparent rounded-full mx-auto mb-4" />
          <p className="text-secondary/60">Φόρτωση κεφαλαίων...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16 text-center">
        <div className="text-5xl mb-4">⚠️</div>
        <p className="text-lg text-error mb-4">{error}</p>
        <Button onClick={() => window.location.reload()}>Δοκίμασε ξανά</Button>
      </div>
    );
  }

  const groupedChapters = {};
  chapters.forEach(ch => {
    const level = ch.difficulty_level;
    if (!groupedChapters[level]) groupedChapters[level] = [];
    groupedChapters[level].push(ch);
  });

  const levelOrder = ['beginner', 'elementary', 'intermediate'];

  return (
    <div className="max-w-4xl mx-auto px-4 py-6 md:py-8">
      {/* Header */}
      <div className="mb-6 md:mb-8">
        <h1 className="text-2xl md:text-3xl font-extrabold text-secondary mb-2">Κεφάλαια</h1>
        <p className="text-secondary/60 mb-4">
          Διάλεξε ένα κεφάλαιο για να ξεκινήσεις τη μάθηση
        </p>
        <ProgressBar value={completedCount} max={chapters.length} size="md" />
      </div>

      {/* Grouped Chapter List */}
      <div className="space-y-8">
        {levelOrder.map(level => {
          const group = groupedChapters[level];
          if (!group || group.length === 0) return null;
          const header = levelHeaders[level];
          const diff = difficultyLabels[level];

          return (
            <div key={level}>
              {/* Level Header */}
              <div className={`bg-gradient-to-r ${header.color} border rounded-xl px-5 py-4 mb-4`}>
                <div className="flex items-center gap-3">
                  <span className="text-2xl">{diff.emoji}</span>
                  <div>
                    <h2 className="font-bold text-secondary">{header.title}</h2>
                    <p className="text-xs text-secondary/50">{header.subtitle}</p>
                  </div>
                </div>
              </div>

              {/* Chapter Cards */}
              <div className="space-y-3">
                {group.map((chapter) => {
                  const unlocked = isChapterUnlocked(chapter);
                  const chProgress = getChapterProgress(chapter.id);
                  const status = getChapterStatus(chProgress, unlocked);
                  const statusInfo = statusConfig[status];
                  const difficulty = difficultyLabels[chapter.difficulty_level] || difficultyLabels.beginner;

                  return (
                    <Card
                      key={chapter.id}
                      hover={unlocked}
                      className={`${!unlocked ? 'opacity-50 grayscale' : ''} transition-all duration-300`}
                    >
                      <div className="flex flex-col sm:flex-row sm:items-center gap-3 sm:gap-4">
                        {/* Chapter number */}
                        <div className={`flex-shrink-0 w-12 h-12 sm:w-14 sm:h-14 rounded-xl flex items-center justify-center text-lg sm:text-xl font-bold
                          ${status === 'completed' ? 'bg-success/20 text-success' :
                            status === 'in_progress' ? 'bg-amber-100 text-amber-700' :
                            unlocked ? 'bg-secondary/10 text-secondary' : 'bg-gray-100 text-gray-400'}`}
                        >
                          {status === 'completed' ? '✓' : chapter.order_index}
                        </div>

                        {/* Chapter info */}
                        <div className="flex-1 min-w-0">
                          <div className="flex items-center gap-2 flex-wrap mb-0.5">
                            <h3 className="text-base sm:text-lg font-bold text-secondary">
                              {chapter.title_greek}
                            </h3>
                            <span className={`px-2 py-0.5 rounded-full text-xs font-medium ${difficulty.color}`}>
                              {difficulty.label}
                            </span>
                          </div>
                          <p className="text-sm text-secondary/50 italic">{chapter.title_spanish}</p>
                          <div className="flex items-center gap-3 mt-1 text-xs text-secondary/50">
                            <span className={statusInfo.color}>
                              {statusInfo.icon} {statusInfo.label}
                            </span>
                            <span>{chapter.section_count} ενότητες</span>
                            {chProgress.lastScore !== null && (
                              <span className={chProgress.lastScore >= 60 ? 'text-success' : 'text-error'}>
                                Βαθμός: {chProgress.lastScore}%
                              </span>
                            )}
                          </div>
                        </div>

                        {/* Actions */}
                        <div className="flex gap-2 flex-shrink-0">
                          {unlocked ? (
                            <>
                              <Link to={`/learn/${chapter.id}`}>
                                <Button variant="primary" size="sm">
                                  Μάθημα
                                </Button>
                              </Link>
                              <Link to={chProgress.lessonViewed ? `/exam/${chapter.id}` : '#'}>
                                <Button
                                  variant="outline"
                                  size="sm"
                                  disabled={!chProgress.lessonViewed}
                                >
                                  Εξέταση
                                </Button>
                              </Link>
                            </>
                          ) : (
                            <Button variant="ghost" size="sm" disabled>
                              🔒 Κλειδωμένο
                            </Button>
                          )}
                        </div>
                      </div>
                    </Card>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
