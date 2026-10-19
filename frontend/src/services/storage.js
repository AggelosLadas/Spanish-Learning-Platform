const STORAGE_KEY = 'espanol_app';

function getStore() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return getDefaultState();
    const parsed = JSON.parse(raw);
    if (!parsed.progress || !parsed.sectionsViewed || !parsed.examHistory) {
      return getDefaultState();
    }
    return parsed;
  } catch {
    return getDefaultState();
  }
}

function saveStore(data) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
}

function getDefaultState() {
  return {
    progress: {},
    sectionsViewed: {},
    examHistory: [],
  };
}

export function getProgress() {
  return getStore().progress;
}

export function getChapterProgress(chapterId) {
  const progress = getStore().progress;
  return progress[String(chapterId)] || {
    lessonViewed: false,
    examPassed: false,
    lastScore: null,
    lastAttemptAt: null,
    attempts: 0,
  };
}

export function setProgress(chapterId, data) {
  const store = getStore();
  const existing = store.progress[String(chapterId)] || {};
  store.progress[String(chapterId)] = { ...existing, ...data };
  saveStore(store);
}

export function getSectionsViewed(chapterId) {
  const store = getStore();
  return store.sectionsViewed[String(chapterId)] || [];
}

export function markSectionViewed(chapterId, sectionId) {
  const store = getStore();
  const key = String(chapterId);
  if (!store.sectionsViewed[key]) {
    store.sectionsViewed[key] = [];
  }
  if (!store.sectionsViewed[key].includes(sectionId)) {
    store.sectionsViewed[key].push(sectionId);
  }
  saveStore(store);
}

export function saveExamResult(result) {
  const store = getStore();
  store.examHistory.push(result);
  saveStore(store);
}

export function getExamHistory() {
  return getStore().examHistory;
}

export function getLatestExamResult(chapterId) {
  const history = getExamHistory();
  const results = history.filter(r => r.chapterId === chapterId);
  return results.length > 0 ? results[results.length - 1] : null;
}

export function resetAll() {
  localStorage.removeItem(STORAGE_KEY);
}

export function getOverallProgress(totalChapters) {
  const progress = getProgress();
  const completed = Object.values(progress).filter(p => p.examPassed).length;
  return totalChapters > 0 ? Math.round((completed / totalChapters) * 100) : 0;
}
