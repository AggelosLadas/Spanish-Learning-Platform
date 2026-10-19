import MultipleChoice from './MultipleChoice';
import TrueFalse from './TrueFalse';
import FillBlank from './FillBlank';
import Translation from './Translation';
import MatchPairs from './MatchPairs';

const questionComponents = {
  multiple_choice: MultipleChoice,
  true_false: TrueFalse,
  fill_blank: FillBlank,
  translation: Translation,
  match: MatchPairs,
};

const typeLabels = {
  multiple_choice: 'Πολλαπλής Επιλογής',
  true_false: 'Σωστό / Λάθος',
  fill_blank: 'Συμπλήρωσε το κενό',
  translation: 'Μετάφραση',
  match: 'Αντιστοίχιση',
};

export default function QuestionCard({
  question,
  questionNumber,
  totalQuestions,
  selectedAnswer,
  onAnswer,
  showFeedback,
}) {
  const Component = questionComponents[question.type];

  if (!Component) {
    return (
      <div className="p-6 bg-error/10 border border-error/30 rounded-xl text-error">
        Άγνωστος τύπος ερώτησης: {question.type}
      </div>
    );
  }

  return (
    <div className="animate-fadeIn">
      {/* Question type badge */}
      <div className="flex items-center gap-2 mb-4">
        <span className="px-3 py-1 bg-secondary/10 text-secondary/70 rounded-full text-xs font-medium">
          {typeLabels[question.type] || question.type}
        </span>
        <span className="text-xs text-secondary/40">
          {question.points} {question.points === 1 ? 'βαθμός' : 'βαθμοί'}
        </span>
      </div>

      {/* Prompt */}
      <h2 className="text-xl font-bold text-secondary mb-6 leading-relaxed">
        {question.prompt}
      </h2>

      {/* Answer component */}
      <Component
        question={question}
        selectedAnswer={selectedAnswer}
        onAnswer={onAnswer}
        showFeedback={showFeedback}
      />

      {/* Feedback explanation */}
      {showFeedback && question.explanation && (
        <div className="mt-5 bg-secondary/5 border border-secondary/10 rounded-xl px-5 py-4">
          <p className="text-sm font-semibold text-secondary/60 mb-1">Εξήγηση:</p>
          <p className="text-secondary/80">{question.explanation}</p>
        </div>
      )}
    </div>
  );
}
