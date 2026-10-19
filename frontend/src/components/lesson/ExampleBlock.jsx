export default function ExampleBlock({ content }) {
  return (
    <div>
      <h2 className="text-2xl font-bold text-secondary mb-4">{content.title}</h2>
      <div className="space-y-3 md:space-y-4">
        {content.examples.map((ex, i) => (
          <div
            key={i}
            className="bg-white rounded-xl border border-neutral/20 overflow-hidden shadow-sm"
          >
            <div className="bg-primary/10 px-4 md:px-5 py-3 md:py-3.5 border-b border-primary/10">
              <p className="text-primary font-semibold text-base md:text-lg whitespace-pre-line leading-relaxed">
                🇪🇸 {ex.spanish}
              </p>
            </div>
            <div className="px-4 md:px-5 py-3 md:py-3.5">
              <p className="text-secondary/80 text-sm md:text-base whitespace-pre-line leading-relaxed">
                🇬🇷 {ex.greek}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
