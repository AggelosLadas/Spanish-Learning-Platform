import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
});

export async function fetchChapters() {
  const { data } = await api.get('/chapters');
  return data;
}

export async function fetchChapter(chapterId) {
  const { data } = await api.get(`/chapters/${chapterId}`);
  return data;
}

export async function fetchChapterSections(chapterId) {
  const { data } = await api.get(`/chapters/${chapterId}/sections`);
  return data;
}

export async function fetchExam(chapterId) {
  const { data } = await api.get(`/exams/${chapterId}`);
  return data;
}

export async function healthCheck() {
  const { data } = await api.get('/health');
  return data;
}

export default api;
