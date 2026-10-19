import { createContext, useContext, useState, useCallback } from 'react';
import * as storage from '../services/storage';

const ProgressContext = createContext(null);

export function ProgressProvider({ children }) {
  const [progress, setProgressState] = useState(() => storage.getProgress());
  const [sectionsViewed, setSectionsViewedState] = useState(() => {
    const store = JSON.parse(localStorage.getItem('espanol_app') || '{}');
    return store.sectionsViewed || {};
  });

  const updateProgress = useCallback((chapterId, data) => {
    storage.setProgress(chapterId, data);
    setProgressState(storage.getProgress());
  }, []);

  const markSectionViewed = useCallback((chapterId, sectionId) => {
    storage.markSectionViewed(chapterId, sectionId);
    setSectionsViewedState(prev => {
      const key = String(chapterId);
      const existing = prev[key] || [];
      if (existing.includes(sectionId)) return prev;
      return { ...prev, [key]: [...existing, sectionId] };
    });
  }, []);

  const getChapterProgress = useCallback((chapterId) => {
    return progress[String(chapterId)] || {
      lessonViewed: false,
      examPassed: false,
      lastScore: null,
      lastAttemptAt: null,
      attempts: 0,
    };
  }, [progress]);

  const getSectionsViewed = useCallback((chapterId) => {
    return sectionsViewed[String(chapterId)] || [];
  }, [sectionsViewed]);

  const resetProgress = useCallback(() => {
    storage.resetAll();
    setProgressState({});
    setSectionsViewedState({});
  }, []);

  const value = {
    progress,
    updateProgress,
    markSectionViewed,
    getChapterProgress,
    getSectionsViewed,
    resetProgress,
  };

  return (
    <ProgressContext.Provider value={value}>
      {children}
    </ProgressContext.Provider>
  );
}

export function useProgress() {
  const context = useContext(ProgressContext);
  if (!context) {
    throw new Error('useProgress must be used within a ProgressProvider');
  }
  return context;
}
