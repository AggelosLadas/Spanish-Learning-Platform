export function normalizeAnswer(answer) {
  if (typeof answer !== 'string') return '';
  return answer.trim().toLowerCase().replace(/\s+/g, ' ');
}

export function checkAnswer(userAnswer, correctAnswer, questionType) {
  if (!userAnswer && userAnswer !== 0) return false;

  const normalized = normalizeAnswer(String(userAnswer));
  const correct = normalizeAnswer(String(correctAnswer));

  if (questionType === 'fill_blank' || questionType === 'translation') {
    return normalized === correct;
  }

  return normalized === correct;
}

export function calculateScore(answers, questions) {
  let correctCount = 0;
  let totalPoints = 0;
  let earnedPoints = 0;

  const details = questions.map((q) => {
    const userAnswer = answers[q.id];
    const isCorrect = checkAnswer(userAnswer, q.correct_answer, q.type);

    totalPoints += q.points;
    if (isCorrect) {
      correctCount++;
      earnedPoints += q.points;
    }

    return {
      questionId: q.id,
      prompt: q.prompt,
      type: q.type,
      userAnswer: userAnswer ?? null,
      correctAnswer: q.correct_answer,
      explanation: q.explanation,
      isCorrect,
      points: q.points,
    };
  });

  const percentage = totalPoints > 0 ? Math.round((earnedPoints / totalPoints) * 100) : 0;

  return {
    correctCount,
    totalQuestions: questions.length,
    earnedPoints,
    totalPoints,
    percentage,
    details,
  };
}

export function getPerformanceLabel(percentage) {
  if (percentage >= 80) return { text: 'Εξαιρετικά! Μπράβο σου!', emoji: '🏆', color: 'text-success' };
  if (percentage >= 60) return { text: 'Καλά! Συνέχισε έτσι.', emoji: '👍', color: 'text-primary' };
  return { text: 'Χρειάζεσαι λίγη εξάσκηση.', emoji: '💪', color: 'text-secondary' };
}
