import { useEffect, useState, useCallback } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import Button from '../components/common/Button';
import QuestionCard from '../components/exam/QuestionCard';
import { fetchExam, fetchChapter } from '../services/api';
import { useProgress } from '../context/ProgressContext';
import { calculateScore, checkAnswer } from '../utils/scoring';
import { saveExamResult } from '../services/storage';

export default function ExamPage() {
  const { chapterId } = useParams();
  const navigate = useNavigate();
  const { updateProgress, getChapterProgress } = useProgress();

  const [exam, setExam] = useState(null);
  const [chapter, setChapter] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [currentIdx, setCurrentIdx] = useState(0);
  const [answers, setAnswers] = useState({});
  const [correctness, setCorrectness] = useState({});
  const [showFeedback, setShowFeedback] = useState(false);
  const [examStarted, setExamStarted] = useState(false);

  useEffect(() => {
    setLoading(true);
    Promise.all([fetchExam(chapterId), fetchChapter(chapterId)])
      .then(([examData, chapterData]) => {
        setExam(examData);
        setChapter(chapterData);
        setLoading(false);
      })
      .catch(() => {
        setError('Σφάλμα κατά τη φόρτωση της εξέτασης.');
        setLoading(false);
      });
  }, [chapterId]);

  const questions = exam?.questions || [];
  const totalQuestions = questions.length;
  const currentQuestion = questions[currentIdx];
  const currentAnswer = currentQuestion ? answers[currentQuestion.id] : undefined;
  const answeredCount = Object.keys(answers).length;
  const isLastQuestion = currentIdx === totalQuestions - 1;

  const handleAnswer = useCallback((answer) => {
    if (!currentQuestion || showFeedback) return;
    setAnswers(prev => ({ ...prev, [currentQuestion.id]: answer }));
    const isCorrect = checkAnswer(answer, currentQuestion.correct_answer, currentQuestion.type);
    setCorrectness(prev => ({ ...prev, [currentQuestion.id]: isCorrect }));
    setShowFeedback(true);
  }, [currentQuestion, showFeedback]);

  const handleNext = () => {
    if (isLastQuestion) {
      const result = calculateScore(answers, questions);
      const passed = result.percentage >= (exam.passing_score_pct || 60);
      const chProgress = getChapterProgress(Number(chapterId));

      saveExamResult({
        examId: exam.id,
        chapterId: Number(chapterId),
        score: result.percentage,
        passed,
        answers,
        completedAt: new Date().toISOString(),
      });

      updateProgress(Number(chapterId), {
        examPassed: passed,
        lastScore: result.percentage,
        lastAttemptAt: new Date().toISOString(),
        attempts: (chProgress.attempts || 0) + 1,
      });

      navigate(`/results/${chapterId}`);
    } else {
      setCurrentIdx(prev => prev + 1);
      setShowFeedback(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="text-center">
          <div className="animate-spin w-12 h-12 border-4 border-primary border-t-transparent rounded-full mx-auto mb-4" />
          <p className="text-secondary/60">Φόρτωση εξέτασης...</p>
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

  if (!examStarted) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16">
        <div className="bg-white rounded-2xl shadow-lg border border-neutral/20 p-8 text-center">
          <div className="text-6xl mb-4">📝</div>
          <h1 className="text-3xl font-extrabold text-secondary mb-2">
            {exam.title}
          </h1>
          {chapter && (
            <p className="text-secondary/50 italic mb-6">
              Κεφάλαιο {chapter.order_index}: {chapter.title_greek}
            </p>
          )}

          <div className="bg-background rounded-xl p-5 mb-6 text-left space-y-3">
            <div className="flex items-center gap-3">
              <span className="text-lg">📊</span>
              <span className="text-secondary/80">
                <strong>{totalQuestions}</strong> ερωτήσεις
              </span>
            </div>
            <div className="flex items-center gap-3">
              <span className="text-lg">🎯</span>
              <span className="text-secondary/80">
                Βαθμός επιτυχίας: <strong>{exam.passing_score_pct}%</strong>
              </span>
            </div>
            <div className="flex items-center gap-3">
              <span className="text-lg">💡</span>
              <span className="text-secondary/80">
                Βλέπεις ανατροφοδότηση μετά από κάθε ερώτηση
              </span>
            </div>
            <div className="flex items-center gap-3">
              <span className="text-lg">⚠️</span>
              <span className="text-secondary/80">
                Δεν μπορείς να γυρίσεις σε προηγούμενη ερώτηση
              </span>
            </div>
          </div>

          <div className="flex gap-3 justify-center">
            <Link to={`/learn/${chapterId}`}>
              <Button variant="ghost">← Πίσω στο μάθημα</Button>
            </Link>
            <Button variant="primary" size="lg" onClick={() => setExamStarted(true)}>
              Ξεκίνα την Εξέταση!
            </Button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto px-4 py-6">
      {/* Top progress area */}
      <div className="mb-6">
        <div className="flex items-center justify-between mb-2">
          <span className="text-sm font-semibold text-secondary">
            Ερώτηση {currentIdx + 1} από {totalQuestions}
          </span>
          <span className="text-sm text-secondary/50">
            {answeredCount} απαντημένες
          </span>
        </div>
        <div className="w-full bg-neutral/30 rounded-full h-3">
          <div
            className="h-3 bg-gradient-to-r from-primary to-primary-dark rounded-full transition-all duration-500"
            style={{ width: `${((currentIdx + 1) / totalQuestions) * 100}%` }}
          />
        </div>
        {/* Dot indicators */}
        <div className="flex gap-1 mt-2 justify-center flex-wrap">
          {questions.map((q, idx) => {
            const isAnswered = q.id in answers;
            const isCurrent = idx === currentIdx;
            const wasCorrect = correctness[q.id];

            let dotColor = 'bg-secondary/15';
            if (isCurrent) {
              dotColor = 'bg-[#d97706] scale-125';
            } else if (isAnswered) {
              dotColor = wasCorrect ? 'bg-success' : 'bg-error';
            }

            return (
              <div
                key={q.id}
                className={`w-2.5 h-2.5 rounded-full transition-all ${dotColor}`}
              />
            );
          })}
        </div>
      </div>

      {/* Question Card */}
      <div className="bg-white rounded-2xl shadow-lg border border-neutral/20 p-6 md:p-8 mb-6">
        {currentQuestion && (
          <QuestionCard
            key={currentQuestion.id}
            question={currentQuestion}
            questionNumber={currentIdx + 1}
            totalQuestions={totalQuestions}
            selectedAnswer={currentAnswer}
            onAnswer={handleAnswer}
            showFeedback={showFeedback}
          />
        )}
      </div>

      {/* Navigation */}
      <div className="flex justify-between items-center">
        <div className="text-sm text-secondary/50">
          {exam.title}
        </div>
        {showFeedback && (
          <Button variant="primary" onClick={handleNext}>
            {isLastQuestion ? 'Δες τα αποτελέσματα →' : 'Επόμενη ερώτηση →'}
          </Button>
        )}
      </div>
    </div>
  );
}
