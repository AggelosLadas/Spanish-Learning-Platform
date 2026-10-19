function extractYouTubeId(urlOrId) {
  if (!urlOrId) return null;

  const trimmed = urlOrId.trim();

  if (/^[a-zA-Z0-9_-]{11}$/.test(trimmed)) {
    return trimmed;
  }

  try {
    const url = new URL(trimmed);
    const host = url.hostname.replace(/^www\./, '');

    if (host === 'youtu.be') {
      return url.pathname.slice(1).split('/')[0] || null;
    }

    if (host === 'youtube.com' || host === 'm.youtube.com') {
      if (url.pathname === '/watch') {
        return url.searchParams.get('v');
      }
      const embedMatch = url.pathname.match(/^\/embed\/([a-zA-Z0-9_-]{11})/);
      if (embedMatch) return embedMatch[1];
      const shortsMatch = url.pathname.match(/^\/shorts\/([a-zA-Z0-9_-]{11})/);
      if (shortsMatch) return shortsMatch[1];
    }
  } catch {
    return null;
  }

  return null;
}

export default function VideoBlock({ content }) {
  const videoId = extractYouTubeId(content.youtube_url || content.video_id);

  if (!videoId) {
    return (
      <div className="p-4 bg-error/10 border border-error/30 rounded-xl text-error">
        Μη έγκυρο URL βίντεο YouTube.
      </div>
    );
  }

  return (
    <div>
      <h2 className="text-2xl font-bold text-secondary mb-4">{content.title}</h2>
      {content.description && (
        <p className="text-secondary/80 text-lg leading-relaxed mb-6">{content.description}</p>
      )}
      <div className="relative w-full rounded-xl overflow-hidden shadow-lg bg-black aspect-video">
        <iframe
          className="absolute inset-0 w-full h-full"
          src={`https://www.youtube.com/embed/${videoId}`}
          title={content.title || 'YouTube video'}
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          allowFullScreen
        />
      </div>
    </div>
  );
}
