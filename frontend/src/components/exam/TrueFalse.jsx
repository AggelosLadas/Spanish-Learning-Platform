export default function TrueFalse({ question, selectedAnswer, onAnswer, showFeedback }) {
  const options = question.options_json || ['Σωστό', 'Λάθος'];

  return (
    <div className="flex gap-4 justify-center">
      {options.map((option) => {
        const isSelected = selectedAnswer === option;
        const isCorrect = option === question.correct_answer;
        const isTrue = option === 'Σωστό';

        let style = isTrue
          ? 'bg-white border-2 border-success/30 hover:bg-success/10 hover:border-success'
          : 'bg-white border-2 border-error/30 hover:bg-error/10 hover:border-error';

        if (showFeedback && isSelected && isCorrect) {
          style = 'bg-success/15 border-2 border-success ring-2 ring-success/20';
        } else if (showFeedback && isSelected && !isCorrect) {
          style = 'bg-error/15 border-2 border-error ring-2 ring-error/20';
        } else if (showFeedback && isCorrect) {
          style = 'bg-success/10 border-2 border-success/50';
        } else if (isSelected) {
          style = isTrue
            ? 'bg-success/15 border-2 border-success ring-2 ring-success/20'
            : 'bg-error/15 border-2 border-error ring-2 ring-error/20';
        }

        return (
          <button
            key={option}
            onClick={() => !showFeedback && onAnswer(option)}
            disabled={showFeedback}
            className={`flex-1 max-w-48 py-6 px-6 rounded-xl text-center transition-all ${style}
              ${showFeedback ? 'cursor-default' : 'cursor-pointer'}`}
          >
            <div className="text-3xl mb-2">{isTrue ? '✓' : '✗'}</div>
            <div className="font-bold text-lg text-secondary">{option}</div>
          </button>
        );
      })}
    </div>
  );
}
