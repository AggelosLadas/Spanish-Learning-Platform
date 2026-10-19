export default function Card({ children, className = '', onClick, hover = true }) {
  return (
    <div
      onClick={onClick}
      className={`bg-white rounded-2xl shadow-md border border-neutral/20 p-6
        ${hover ? 'hover:shadow-lg hover:-translate-y-0.5 transition-all duration-200' : ''}
        ${onClick ? 'cursor-pointer' : ''}
        ${className}`}
    >
      {children}
    </div>
  );
}
