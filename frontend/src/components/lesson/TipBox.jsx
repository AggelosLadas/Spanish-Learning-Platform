export default function TipBox({ content }) {
  return (
    <div>
      <h2 className="text-2xl font-bold text-secondary mb-4">{content.title}</h2>
      <div className="bg-amber-50 border border-amber-200 rounded-xl p-5 space-y-3">
        {content.tips.map((tip, i) => (
          <div key={i} className="flex gap-3 items-start">
            <span className="flex-shrink-0 text-lg mt-0.5">💡</span>
            <p className="text-secondary/85 leading-relaxed">{tip}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
