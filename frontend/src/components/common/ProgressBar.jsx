export default function ProgressBar({ value, max = 100, className = '', showLabel = true, size = 'md' }) {
  const percentage = max > 0 ? Math.round((value / max) * 100) : 0;

  const heights = {
    sm: 'h-2',
    md: 'h-3',
    lg: 'h-4',
  };

  return (
    <div className={`w-full ${className}`}>
      {showLabel && (
        <div className="flex justify-between mb-1 text-sm text-secondary/70">
          <span>Πρόοδος</span>
          <span className="font-semibold">{percentage}%</span>
        </div>
      )}
      <div className={`w-full bg-neutral/40 rounded-full overflow-hidden ${heights[size]}`}>
        <div
          className={`${heights[size]} bg-gradient-to-r from-primary to-primary-dark rounded-full transition-all duration-500 ease-out`}
          style={{ width: `${percentage}%` }}
        />
      </div>
    </div>
  );
}
