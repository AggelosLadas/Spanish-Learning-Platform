import { useState } from 'react';

export default function Translation({ question, selectedAnswer, onAnswer, showFeedback }) {
  const [value, setValue] = useState(selectedAnswer || '');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (value.trim() && !showFeedback) {
      onAnswer(value.trim());
    }
  };

  let inputStyle = 'border-2 border-secondary/20 focus:border-primary focus:ring-2 focus:ring-primary/20';
  if (showFeedback) {
    const isCorrect = value.trim().toLowerCase() === question.correct_answer.toLowerCase();
    inputStyle = isCorrect
      ? 'border-2 border-success bg-success/5 ring-2 ring-success/20'
      : 'border-2 border-error bg-error/5 ring-2 ring-error/20';
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="bg-secondary/5 rounded-xl px-5 py-3 mb-2">
        <p className="text-sm text-secondary/60">Μετάφρασε:</p>
      </div>

      <textarea
        value={value}
        onChange={(e) => {
          setValue(e.target.value);
          if (selectedAnswer) onAnswer(e.target.value.trim());
        }}
        disabled={showFeedback}
        placeholder="Γράψε τη μετάφραση..."
        rows={2}
        autoFocus
        className={`w-full px-5 py-4 rounded-xl text-lg outline-none transition-all resize-none ${inputStyle}
          ${showFeedback ? 'cursor-default' : ''}`}
        autoComplete="off"
        spellCheck="false"
      />

      {showFeedback && selectedAnswer?.toLowerCase() !== question.correct_answer.toLowerCase() && (
        <div className="bg-success/10 border border-success/30 rounded-xl px-5 py-3">
          <p className="text-sm text-secondary/60 mb-1">Σωστή απάντηση:</p>
          <p className="font-bold text-success text-lg">{question.correct_answer}</p>
        </div>
      )}

      {!showFeedback && !selectedAnswer && (
        <button
          type="submit"
          disabled={!value.trim()}
          className={`w-full py-3 rounded-xl font-semibold text-white transition-all
            ${value.trim()
              ? 'bg-primary hover:bg-primary-dark shadow-md'
              : 'bg-secondary/20 cursor-not-allowed'}`}
        >
          Υποβολή
        </button>
      )}
    </form>
  );
}
