export default function MultipleChoice({ question, selectedAnswer, onAnswer, showFeedback }) {
  const options = question.options_json || [];

  return (
    <div className="space-y-3">
      {options.map((option, idx) => {
        const isSelected = selectedAnswer === option;
        const isCorrect = option === question.correct_answer;
        let style = 'bg-white border-2 border-secondary/15 hover:border-primary/40 hover:bg-primary/5';

        if (showFeedback && isSelected && isCorrect) {
          style = 'bg-success/10 border-2 border-success ring-2 ring-success/20';
        } else if (showFeedback && isSelected && !isCorrect) {
          style = 'bg-error/10 border-2 border-error ring-2 ring-error/20';
        } else if (showFeedback && isCorrect) {
          style = 'bg-success/10 border-2 border-success/50';
        } else if (isSelected) {
          style = 'bg-primary/10 border-2 border-primary ring-2 ring-primary/20';
        }

        return (
          <button
            key={idx}
            onClick={() => !showFeedback && onAnswer(option)}
            disabled={showFeedback}
            className={`w-full text-left px-5 py-4 rounded-xl transition-all text-base ${style}
              ${showFeedback ? 'cursor-default' : 'cursor-pointer'}`}
          >
            <div className="flex items-center gap-3">
              <span className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold border-2
                ${isSelected
                  ? showFeedback
                    ? isCorrect ? 'bg-success text-white border-success' : 'bg-error text-white border-error'
                    : 'bg-primary text-white border-primary'
                  : showFeedback && isCorrect
                    ? 'bg-success/20 text-success border-success/50'
                    : 'bg-secondary/5 text-secondary/60 border-secondary/20'
                }`}>
                {showFeedback && isSelected ? (isCorrect ? '✓' : '✗') : String.fromCharCode(65 + idx)}
              </span>
              <span className="font-medium text-secondary">{option}</span>
            </div>
          </button>
        );
      })}
    </div>
  );
}
