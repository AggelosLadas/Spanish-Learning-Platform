export default function GrammarBox({ content }) {
  return (
    <div>
      <h2 className="text-2xl font-bold text-secondary mb-4">{content.title}</h2>
      {content.body && (
        <p className="text-secondary/80 mb-4 leading-relaxed">{content.body}</p>
      )}
      <div className="bg-secondary/5 border-l-4 border-primary rounded-r-xl p-4 md:p-5 space-y-2 md:space-y-2.5">
        {content.rules.map((rule, i) => (
          <div key={i} className="flex gap-2.5 md:gap-3 items-start">
            <span className="flex-shrink-0 w-5 h-5 md:w-6 md:h-6 bg-primary/15 text-primary rounded-full flex items-center justify-center text-xs font-bold mt-0.5">
              {i + 1}
            </span>
            <p className="text-secondary/90 leading-relaxed text-sm md:text-base">{rule}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
