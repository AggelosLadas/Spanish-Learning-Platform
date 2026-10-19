export default function VocabTable({ content }) {
  return (
    <div>
      <h2 className="text-2xl font-bold text-secondary mb-4">{content.title}</h2>

      {/* Desktop table */}
      <div className="hidden sm:block overflow-x-auto rounded-xl border border-neutral/30">
        <table className="w-full">
          <thead>
            <tr className="bg-secondary text-white text-left">
              <th className="px-5 py-3 font-semibold text-sm">Ελληνικά</th>
              <th className="px-5 py-3 font-semibold text-sm">Ισπανικά</th>
              <th className="px-5 py-3 font-semibold text-sm">Προφορά</th>
            </tr>
          </thead>
          <tbody>
            {content.words.map((word, i) => (
              <tr
                key={i}
                className={`border-t border-neutral/20 transition-colors hover:bg-primary/5 ${
                  i % 2 === 0 ? 'bg-white' : 'bg-background/50'
                }`}
              >
                <td className="px-5 py-3.5 text-secondary font-medium">{word.greek}</td>
                <td className="px-5 py-3.5 text-primary font-bold text-lg">{word.spanish}</td>
                <td className="px-5 py-3.5 text-secondary/60 italic">{word.pronunciation}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Mobile cards */}
      <div className="sm:hidden space-y-2">
        {content.words.map((word, i) => (
          <div key={i} className="bg-white rounded-xl border border-neutral/20 p-4 hover:shadow-sm transition-shadow">
            <div className="text-primary font-bold text-lg mb-1">{word.spanish}</div>
            <div className="text-secondary font-medium text-sm">{word.greek}</div>
            <div className="text-secondary/50 italic text-xs mt-1">🔊 {word.pronunciation}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
