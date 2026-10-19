import { useState, useEffect } from 'react';

function shuffleArray(arr) {
  const shuffled = [...arr];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled;
}

export default function MatchPairs({ question, selectedAnswer, onAnswer, showFeedback }) {
  const pairs = question.options_json || [];
  const [leftItems] = useState(() => pairs.map(p => p.left || p[0]));
  const [rightItems] = useState(() => shuffleArray(pairs.map(p => p.right || p[1])));
  const [matches, setMatches] = useState({});
  const [selectedLeft, setSelectedLeft] = useState(null);

  useEffect(() => {
    if (selectedAnswer && typeof selectedAnswer === 'object') {
      setMatches(selectedAnswer);
    }
  }, []);

  const correctMap = {};
  pairs.forEach(p => {
    correctMap[p.left || p[0]] = p.right || p[1];
  });

  const handleLeftClick = (item) => {
    if (showFeedback) return;
    setSelectedLeft(selectedLeft === item ? null : item);
  };

  const handleRightClick = (item) => {
    if (showFeedback || !selectedLeft) return;

    const newMatches = { ...matches, [selectedLeft]: item };
    setMatches(newMatches);
    setSelectedLeft(null);

    if (Object.keys(newMatches).length === leftItems.length) {
      const answerStr = leftItems.map(l => `${l}:${newMatches[l]}`).join('|');
      const correctStr = leftItems.map(l => `${l}:${correctMap[l]}`).join('|');
      onAnswer(answerStr);
    }
  };

  const removeMatch = (leftKey) => {
    if (showFeedback) return;
    const newMatches = { ...matches };
    delete newMatches[leftKey];
    setMatches(newMatches);
  };

  const matchedRight = new Set(Object.values(matches));

  return (
    <div className="space-y-4">
      <p className="text-sm text-secondary/60 text-center mb-2">
        Επίλεξε ένα στοιχείο αριστερά και μετά αντιστοίχισέ το δεξιά
      </p>

      <div className="grid grid-cols-2 gap-4">
        {/* Left column */}
        <div className="space-y-2">
          {leftItems.map((item) => {
            const isMatched = item in matches;
            const isActive = selectedLeft === item;
            let itemCorrect = false;
            if (showFeedback && isMatched) {
              itemCorrect = matches[item] === correctMap[item];
            }

            let style = 'bg-white border-2 border-secondary/15 hover:border-primary/40';
            if (showFeedback && isMatched) {
              style = itemCorrect
                ? 'bg-success/10 border-2 border-success'
                : 'bg-error/10 border-2 border-error';
            } else if (isMatched) {
              style = 'bg-primary/10 border-2 border-primary/40';
            } else if (isActive) {
              style = 'bg-primary/15 border-2 border-primary ring-2 ring-primary/20';
            }

            return (
              <button
                key={item}
                onClick={() => isMatched ? removeMatch(item) : handleLeftClick(item)}
                disabled={showFeedback}
                className={`w-full text-left px-4 py-3 rounded-xl transition-all text-sm font-medium ${style}
                  ${showFeedback ? 'cursor-default' : 'cursor-pointer'}`}
              >
                <span className="text-secondary">{item}</span>
                {isMatched && (
                  <span className="ml-2 text-xs text-secondary/40">→ {matches[item]}</span>
                )}
              </button>
            );
          })}
        </div>

        {/* Right column */}
        <div className="space-y-2">
          {rightItems.map((item) => {
            const isUsed = matchedRight.has(item);
            let style = selectedLeft
              ? 'bg-white border-2 border-primary/30 hover:bg-primary/10 hover:border-primary'
              : 'bg-white border-2 border-secondary/15';

            if (isUsed) {
              style = 'bg-secondary/5 border-2 border-secondary/10 opacity-50';
            }

            return (
              <button
                key={item}
                onClick={() => handleRightClick(item)}
                disabled={showFeedback || isUsed || !selectedLeft}
                className={`w-full text-left px-4 py-3 rounded-xl transition-all text-sm font-medium ${style}
                  ${showFeedback || isUsed || !selectedLeft ? 'cursor-default' : 'cursor-pointer'}`}
              >
                <span className="text-secondary">{item}</span>
              </button>
            );
          })}
        </div>
      </div>

      {showFeedback && (
        <div className="bg-secondary/5 rounded-xl p-4 mt-4">
          <p className="text-sm font-semibold text-secondary mb-2">Σωστές αντιστοιχίσεις:</p>
          <div className="space-y-1">
            {pairs.map((p, i) => (
              <p key={i} className="text-sm text-secondary/80">
                {p.left || p[0]} → {p.right || p[1]}
              </p>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
