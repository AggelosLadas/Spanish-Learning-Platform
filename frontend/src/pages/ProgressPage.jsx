import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import ProgressBar from '../components/common/ProgressBar';
import Modal from '../components/common/Modal';
import { fetchChapters, fetchExam } from '../services/api';
import { useProgress } from '../context/ProgressContext';
import { getExamHistory, getLatestExamResult } from '../services/storage';
import { checkAnswer } from '../utils/scoring';

const difficultyLabels = {
  beginner: 'Αρχάριος',
  elementary: 'Βασικός',
  intermediate: 'Μέσος',
};

const statusConfig = {
  not_started: { label: 'Δεν ξεκίνησε', badge: 'bg-secondary/10 text-secondary/60' },
  in_progress: { label: 'Σε εξέλιξη', badge: 'bg-amber-100 text-amber-700' },
  completed: { label: 'Ολοκληρώθηκε', badge: 'bg-success/15 text-success' },
};

function ChapterDetails({ chapterId }) {
  const [exam, setExam] = useState(null);
  const [loading, setLoading] = useState(true);
  const examResult = getLatestExamResult(chapterId);

  useEffect(() => {
    fetchExam(chapterId)
      .then((data) => { setExam(data); setLoading(false); })
      .catch(() => setLoading(false));
  }, [chapterId]);

  if (loading) {
    return (
      <div className="py-6 text-center">
        <div className="animate-spin w-6 h-6 border-2 border-primary border-t-transparent rounded-full mx-auto" />
      </div>
    );
  }

  if (!examResult) {
    return (
      <div className="py-6 text-center text-secondary/50">
        <p className="mb-3">Δεν υπάρχουν αποτελέσματα ακόμα για αυτό το κεφάλαιο.</p>
        <Link to={`/learn/${chapterId}`}>
          <Button variant="primary" size="sm">Ξεκίνα το μάθημα →</Button>
        </Link>
      </div>
    );
  }

  const questions = exam?.questions || [];
  const { answers, score, passed, completedAt } = examResult;

  const reviewDetails = questions.map((q) => {
    const userAnswer = answers?.[q.id];
    const isCorrect = checkAnswer(userAnswer, q.correct_answer, q.type);
    return { ...q, userAnswer, isCorrect };
  });

  const correctCount = reviewDetails.filter(d => d.isCorrect).length;
  const dateStr = completedAt
    ? new Date(completedAt).toLocaleDateString('el-GR', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' })
    : '';

  return (
    <div className="py-4 space-y-4 animate-fadeIn">
      {/* Summary */}
      <div className="flex flex-wrap items-center gap-3 sm:gap-4">
        <div className="flex items-center gap-2">
          <span className={`text-2xl font-extrabold ${passed ? 'text-success' : 'text-error'}`}>{score}%</span>
          <span className={`px-2 py-0.5 rounded-full text-xs font-semibold ${passed ? 'bg-success/15 text-success' : 'bg-error/15 text-error'}`}>
            {passed ? 'Πέρασε' : 'Δεν πέρασε'}
          </span>
        </div>
        <span className="text-sm text-secondary/50">{correctCount}/{questions.length} σωστές</span>
        {dateStr && <span className="text-xs text-secondary/40">{dateStr}</span>}
        <div className="sm:ml-auto flex gap-2">
          <Link to={`/exam/${chapterId}`}>
            <Button variant="outline" size="sm">🔄 Ξανά</Button>
          </Link>
          <Link to={`/results/${chapterId}`}>
            <Button variant="ghost" size="sm">Πλήρη αποτελέσματα →</Button>
          </Link>
        </div>
      </div>

      {/* Question list */}
      <div className="space-y-2">
        {reviewDetails.map((q) => (
          <div
            key={q.id}
            className={`flex items-start gap-3 px-4 py-3 rounded-xl border ${
              q.isCorrect ? 'bg-success/5 border-success/20' : 'bg-error/5 border-error/20'
            }`}
          >
            <span className={`flex-shrink-0 w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold text-white mt-0.5
              ${q.isCorrect ? 'bg-success' : 'bg-error'}`}>
              {q.isCorrect ? '✓' : '✗'}
            </span>
            <div className="flex-1 min-w-0">
              <p className="text-sm text-secondary font-medium">{q.prompt}</p>
              <div className="flex flex-wrap gap-x-4 gap-y-1 mt-1 text-xs">
                <span>
                  <span className="text-secondary/50">Απάντηση: </span>
                  <span className={q.isCorrect ? 'text-success font-semibold' : 'text-error font-semibold'}>
                    {q.userAnswer || '—'}
                  </span>
                </span>
                {!q.isCorrect && (
                  <span>
                    <span className="text-secondary/50">Σωστό: </span>
                    <span className="text-success font-semibold">{q.correct_answer}</span>
                  </span>
                )}
              </div>
              {q.explanation && !q.isCorrect && (
                <p className="text-xs text-secondary/40 mt-1 italic">💡 {q.explanation}</p>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default function ProgressPage() {
  const [chapters, setChapters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showReset, setShowReset] = useState(false);
  const [expandedChapter, setExpandedChapter] = useState(null);
  const { progress, getChapterProgress, resetProgress } = useProgress();

  useEffect(() => {
    fetchChapters()
      .then((data) => { setChapters(data); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  const examHistory = getExamHistory();
  const totalChapters = chapters.length;
  const completedCount = Object.values(progress).filter(p => p.examPassed).length;
  const inProgressCount = Object.values(progress).filter(p => !p.examPassed && (p.lessonViewed || p.lastScore !== null)).length;
  const totalAttempts = examHistory.length;
  const avgScore = totalAttempts > 0
    ? Math.round(examHistory.reduce((sum, e) => sum + e.score, 0) / totalAttempts)
    : 0;

  const handleReset = () => {
    resetProgress();
    setShowReset(false);
    setExpandedChapter(null);
  };

  const toggleChapter = (chId) => {
    setExpandedChapter(expandedChapter === chId ? null : chId);
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="animate-spin w-12 h-12 border-4 border-primary border-t-transparent rounded-full mx-auto" />
      </div>
    );
  }

  return (
    <div className="max-w-5xl mx-auto px-4 py-8">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8">
        <div>
          <h1 className="text-3xl font-extrabold text-secondary">Η Πρόοδός μου</h1>
          <p className="text-secondary/60 mt-1">Παρακολούθησε τη μαθησιακή σου πορεία</p>
        </div>
        <Button variant="outline" size="sm" onClick={() => setShowReset(true)} className="text-error border-error hover:bg-error hover:text-white">
          🗑️ Επαναφορά Προόδου
        </Button>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <Card hover={false} className="text-center py-5">
          <div className="text-3xl font-extrabold text-primary">{Math.round((completedCount / (totalChapters || 1)) * 100)}%</div>
          <div className="text-xs text-secondary/50 mt-1">Συνολική Πρόοδος</div>
        </Card>
        <Card hover={false} className="text-center py-5">
          <div className="text-3xl font-extrabold text-success">{completedCount}</div>
          <div className="text-xs text-secondary/50 mt-1">Ολοκληρωμένα</div>
        </Card>
        <Card hover={false} className="text-center py-5">
          <div className="text-3xl font-extrabold text-amber-600">{inProgressCount}</div>
          <div className="text-xs text-secondary/50 mt-1">Σε Εξέλιξη</div>
        </Card>
        <Card hover={false} className="text-center py-5">
          <div className="text-3xl font-extrabold text-secondary">{avgScore}%</div>
          <div className="text-xs text-secondary/50 mt-1">Μέσος Βαθμός</div>
        </Card>
      </div>

      {/* Overall Progress */}
      <Card hover={false} className="mb-8">
        <h2 className="font-bold text-secondary mb-3">Συνολική Πρόοδος</h2>
        <ProgressBar value={completedCount} max={totalChapters} size="lg" />
        <p className="text-sm text-secondary/50 mt-2">
          {completedCount} από {totalChapters} κεφάλαια ολοκληρωμένα
          {totalAttempts > 0 && ` · ${totalAttempts} συνολικές προσπάθειες εξέτασης`}
        </p>
      </Card>

      {/* Chapter List - expandable */}
      <Card hover={false} className="overflow-hidden p-0">
        <div className="px-6 py-4 border-b border-neutral/20">
          <h2 className="font-bold text-secondary">Αναλυτικά ανά Κεφάλαιο</h2>
          <p className="text-xs text-secondary/40 mt-0.5">Πάτα σε ένα κεφάλαιο για να δεις τα αποτελέσματα</p>
        </div>

        {/* Header row */}
        <div className="hidden sm:grid grid-cols-[3rem_1fr_5rem_7rem_4rem] md:grid-cols-[3rem_1fr_5rem_7rem_4rem_5rem_6rem] bg-secondary/5 text-sm text-secondary/70 font-semibold">
          <div className="px-4 py-3">#</div>
          <div className="px-4 py-3">Κεφάλαιο</div>
          <div className="px-4 py-3">Επίπεδο</div>
          <div className="px-4 py-3">Κατάσταση</div>
          <div className="px-4 py-3 text-center">Βαθμός</div>
          <div className="px-4 py-3 text-center hidden md:block">Προσπ.</div>
          <div className="px-4 py-3 hidden md:block">Ημ/νία</div>
        </div>

        {/* Rows */}
        <div className="divide-y divide-neutral/10">
          {chapters.map((ch) => {
            const cp = getChapterProgress(ch.id);
            let status = 'not_started';
            if (cp.examPassed) status = 'completed';
            else if (cp.lessonViewed || cp.lastScore !== null) status = 'in_progress';
            const sInfo = statusConfig[status];
            const isExpanded = expandedChapter === ch.id;

            const lastDate = cp.lastAttemptAt
              ? new Date(cp.lastAttemptAt).toLocaleDateString('el-GR', { day: '2-digit', month: '2-digit', year: 'numeric' })
              : '—';

            return (
              <div key={ch.id}>
                {/* Row */}
                <div
                  onClick={() => toggleChapter(ch.id)}
                  className={`cursor-pointer transition-colors ${isExpanded ? 'bg-primary/5' : 'hover:bg-secondary/5'}`}
                >
                  {/* Mobile layout */}
                  <div className="sm:hidden px-4 py-4 flex items-center gap-3">
                    <div className="flex-shrink-0 w-8 h-8 rounded-lg bg-secondary/10 flex items-center justify-center text-sm font-bold text-secondary/60">
                      {ch.order_index}
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="font-semibold text-secondary text-sm truncate">{ch.title_greek}</div>
                      <div className="flex items-center gap-2 mt-0.5">
                        <span className={`px-2 py-0.5 rounded-full text-[10px] font-semibold ${sInfo.badge}`}>{sInfo.label}</span>
                        {cp.lastScore !== null && (
                          <span className={`text-xs font-bold ${cp.lastScore >= 80 ? 'text-success' : cp.lastScore >= 60 ? 'text-amber-600' : 'text-error'}`}>
                            {cp.lastScore}%
                          </span>
                        )}
                      </div>
                    </div>
                    <svg className={`w-4 h-4 text-secondary/40 transition-transform duration-200 flex-shrink-0 ${isExpanded ? 'rotate-180' : ''}`}
                      fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                    </svg>
                  </div>

                  {/* Desktop layout */}
                  <div className="hidden sm:grid grid-cols-[3rem_1fr_5rem_7rem_4rem] md:grid-cols-[3rem_1fr_5rem_7rem_4rem_5rem_6rem] items-center">
                    <div className="px-4 py-4 text-sm font-bold text-secondary/50">{ch.order_index}</div>
                    <div className="px-4 py-4">
                      <div className="font-semibold text-secondary text-sm">{ch.title_greek}</div>
                      <div className="text-xs text-secondary/40 italic">{ch.title_spanish}</div>
                    </div>
                    <div className="px-4 py-4">
                      <span className="text-xs text-secondary/50">{difficultyLabels[ch.difficulty_level]}</span>
                    </div>
                    <div className="px-4 py-4">
                      <span className={`inline-block px-2.5 py-1 rounded-full text-xs font-semibold ${sInfo.badge}`}>
                        {sInfo.label}
                      </span>
                    </div>
                    <div className="px-4 py-4 text-center">
                      {cp.lastScore !== null ? (
                        <span className={`font-bold text-sm ${cp.lastScore >= 80 ? 'text-success' : cp.lastScore >= 60 ? 'text-amber-600' : 'text-error'}`}>
                          {cp.lastScore}%
                        </span>
                      ) : (
                        <span className="text-secondary/30">—</span>
                      )}
                    </div>
                    <div className="px-4 py-4 text-center hidden md:flex items-center justify-between">
                      <span className="text-sm text-secondary/60">{cp.attempts || 0}</span>
                    </div>
                    <div className="px-4 py-4 hidden md:flex items-center justify-between">
                      <span className="text-xs text-secondary/40">{lastDate}</span>
                      <svg className={`w-4 h-4 text-secondary/40 transition-transform duration-200 ${isExpanded ? 'rotate-180' : ''}`}
                        fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                      </svg>
                    </div>
                  </div>
                </div>

                {/* Expanded content */}
                {isExpanded && (
                  <div className="bg-secondary/[0.02] border-t border-neutral/10 px-4 sm:px-6">
                    <ChapterDetails chapterId={ch.id} />
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </Card>

      {/* Reset Modal */}
      <Modal isOpen={showReset} onClose={() => setShowReset(false)} title="Επαναφορά Προόδου">
        <div className="text-center">
          <div className="text-5xl mb-4">⚠️</div>
          <p className="text-secondary/80 mb-2">
            Είσαι σίγουρος ότι θέλεις να διαγράψεις <strong>όλη</strong> την πρόοδό σου;
          </p>
          <p className="text-sm text-secondary/50 mb-6">
            Αυτή η ενέργεια δεν μπορεί να αναιρεθεί. Όλοι οι βαθμοί, τα ολοκληρωμένα
            κεφάλαια και το ιστορικό εξετάσεων θα χαθούν.
          </p>
          <div className="flex gap-3 justify-center">
            <Button variant="ghost" onClick={() => setShowReset(false)}>
              Ακύρωση
            </Button>
            <Button
              variant="primary"
              onClick={handleReset}
              className="!bg-error hover:!bg-red-700"
            >
              Ναι, Διέγραψε τα Πάντα
            </Button>
          </div>
        </div>
      </Modal>
    </div>
  );
}
