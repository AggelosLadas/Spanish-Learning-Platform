export default function TextBlock({ content }) {
  return (
    <div className="prose max-w-none">
      <h2 className="text-2xl font-bold text-secondary mb-4">{content.title}</h2>
      <p className="text-secondary/80 text-lg leading-relaxed">{content.body}</p>
    </div>
  );
}
