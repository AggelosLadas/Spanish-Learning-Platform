import { useEffect, useState } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import Button from '../components/common/Button';
import Card from '../components/common/Card';
import { getLatestExamResult } from '../services/storage';
import { getPerformanceLabel } from '../utils/scoring';
import { fetchExam, fetchChapters } from '../services/api';
import { useProgress } from '../context/ProgressContext';
import { checkAnswer } from '../utils/scoring';

export default function ResultsPage() {
  const { chapterId } = useParams();
  const navigate = useNavigate();
  const { getChapterProgress } = useProgress();

  const [examResult, setExamResult] = useState(null);
  const [exam, setExam] = useState(null);
  const [chapters, setChapters] = useState([]);
  const [showReview, setShowReview] = useState(false);

  useEffect(() => {
    const result = getLatestExamResult(Number(chapterId));
    setExamResult(result);

    fetchExam(chapterId).then(setExam).catch(() => {});
    fetchChapters().then(setChapters).catch(() => {});
  }, [chapterId]);

  if (!examResult) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16 text-center">
        <div className="text-6xl mb-4">🤔</div>
        <h1 className="text-2xl font-bold text-secondary mb-4">
          Δεν βρέθηκαν αποτελέσματα
        </h1>
        <p className="text-secondary/60 mb-6">
          Δεν βρέθηκε αποτέλεσμα εξέτασης για αυτό το κεφάλαιο.
        </p>
        <Link to="/learn">
          <Button variant="outline">← Πίσω στα Κεφάλαια</Button>
        </Link>
      </div>
    );
  }

  const { score, passed } = examResult;
  const performance = getPerformanceLabel(score);
  const questions = exam?.questions || [];

  const currentChapter = chapters.find(c => c.id === Number(chapterId));
  const nextChapter = chapters.find(
    c => currentChapter && c.order_index === currentChapter.order_index + 1
  );

  const reviewDetails = questions.map((q) => {
    const userAnswer = examResult.answers?.[q.id];
    const isCorrect = checkAnswer(userAnswer, q.correct_answer, q.type);
    return { ...q, userAnswer, isCorrect };
  });

  const correctCount = reviewDetails.filter(d => d.isCorrect).length;

  return (
    <div className="max-w-3xl mx-auto px-4 py-8">
      {/* Score Card */}
      <div className="bg-white rounded-2xl shadow-lg border border-neutral/20 p-8 text-center mb-8">
        <div className="text-7xl mb-4">{performance.emoji}</div>

        {/* Score Circle */}
        <div className="relative w-36 h-36 mx-auto mb-6">
          <svg className="w-full h-full -rotate-90" viewBox="0 0 120 120">
            <circle
              cx="60" cy="60" r="52"
              fill="none"
              stroke="currentColor"
              className="text-neutral/30"
              strokeWidth="10"
            />
            <circle
              cx="60" cy="60" r="52"
              fill="none"
              stroke="currentColor"
              className={passed ? 'text-success' : 'text-primary'}
              strokeWidth="10"
              strokeLinecap="round"
              strokeDasharray={`${(score / 100) * 327} 327`}
              style={{ transition: 'stroke-dasharray 1s ease-out' }}
            />
          </svg>
          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="text-3xl font-extrabold text-secondary">{score}%</span>
            <span className="text-xs text-secondary/50">{correctCount}/{questions.length}</span>
          </div>
        </div>

        <h1 className={`text-2xl font-extrabold mb-2 ${performance.color}`}>
          {performance.text}
        </h1>

        <p className="text-secondary/60 mb-2">
          {passed ? (
            <>Πέρασες με <strong>{score}%</strong>!</>
          ) : (
            <>Χρειάζεσαι τουλάχιστον <strong>{exam?.passing_score_pct || 60}%</strong> για να περάσεις.</>
          )}
        </p>

        {currentChapter && (
          <p className="text-sm text-secondary/40 italic">
            {currentChapter.title_greek} — {currentChapter.title_spanish}
          </p>
        )}
      </div>

      {/* Action Buttons */}
      <div className="flex flex-col sm:flex-row gap-3 justify-center mb-8">
        <Button
          variant="outline"
          onClick={() => navigate(`/exam/${chapterId}`)}
        >
          🔄 Επανάληψη Εξέτασης
        </Button>

        {passed && nextChapter && (
          <Button
            variant="success"
            onClick={() => navigate(`/learn/${nextChapter.id}`)}
          >
            Επόμενο Κεφάλαιο →
          </Button>
        )}

        <Link to="/learn">
          <Button variant="ghost">
            📚 Επιστροφή στα Κεφάλαια
          </Button>
        </Link>
      </div>

      {/* Review Section */}
      <div className="mb-4">
        <button
          onClick={() => setShowReview(!showReview)}
          className="w-full flex items-center justify-between bg-white rounded-xl px-6 py-4 shadow-sm border border-neutral/20 hover:bg-secondary/5 transition-colors"
        >
          <span className="font-bold text-secondary">
            📋 Αναλυτικά Αποτελέσματα
          </span>
          <svg
            className={`w-5 h-5 text-secondary/50 transition-transform ${showReview ? 'rotate-180' : ''}`}
            fill="none" stroke="currentColor" viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </button>
      </div>

      {showReview && (
        <div className="space-y-3 animate-fadeIn">
          {reviewDetails.map((q, idx) => (
            <Card key={q.id} hover={false} className={`border-l-4 ${q.isCorrect ? 'border-l-success' : 'border-l-error'}`}>
              <div className="flex items-start gap-3">
                <span className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold text-white
                  ${q.isCorrect ? 'bg-success' : 'bg-error'}`}>
                  {q.isCorrect ? '✓' : '✗'}
                </span>
                <div className="flex-1 min-w-0">
                  <p className="font-semibold text-secondary text-sm mb-1">
                    Ερώτηση {idx + 1}
                  </p>
                  <p className="text-secondary/80 mb-2">{q.prompt}</p>

                  <div className="space-y-1 text-sm">
                    <p>
                      <span className="text-secondary/50">Η απάντησή σου: </span>
                      <span className={q.isCorrect ? 'text-success font-semibold' : 'text-error font-semibold'}>
                        {q.userAnswer || '—'}
                      </span>
                    </p>
                    {!q.isCorrect && (
                      <p>
                        <span className="text-secondary/50">Σωστή απάντηση: </span>
                        <span className="text-success font-semibold">{q.correct_answer}</span>
                      </p>
                    )}
                    {q.explanation && (
                      <p className="text-secondary/50 italic mt-1">💡 {q.explanation}</p>
                    )}
                  </div>
                </div>
              </div>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}
