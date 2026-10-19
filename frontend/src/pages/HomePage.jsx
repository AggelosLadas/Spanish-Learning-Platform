import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import ProgressBar from '../components/common/ProgressBar';
import { fetchChapters } from '../services/api';
import { useProgress } from '../context/ProgressContext';

export default function HomePage() {
  const [chapters, setChapters] = useState([]);
  const [loading, setLoading] = useState(true);
  const { progress } = useProgress();

  useEffect(() => {
    fetchChapters()
      .then((data) => { setChapters(data); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  const totalChapters = chapters.length;
  const completedChapters = Object.values(progress).filter(p => p.examPassed).length;

  const nextChapter = chapters.find((ch) => {
    const cp = progress[String(ch.id)];
    return !cp?.examPassed;
  });

  return (
    <div className="min-h-[calc(100vh-4rem)]">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-br from-secondary via-secondary-light to-secondary overflow-hidden">
        <div className="absolute inset-0 opacity-10">
          <div className="absolute top-6 left-6 md:top-10 md:left-10 text-7xl md:text-9xl select-none">🇪🇸</div>
          <div className="absolute bottom-6 right-6 md:bottom-10 md:right-10 text-7xl md:text-9xl select-none">🇬🇷</div>
        </div>
        <div className="relative max-w-6xl mx-auto px-4 py-14 md:py-20 text-center text-white">
          <h1 className="text-3xl sm:text-4xl md:text-6xl font-extrabold mb-4 tracking-tight animate-fadeIn">
            Μάθε Ισπανικά
            <span className="block text-primary mt-2">βήμα-βήμα</span>
          </h1>
          <p className="text-base md:text-xl text-white/80 max-w-2xl mx-auto mb-8 animate-fadeIn">
            Η πιο εύκολη πλατφόρμα για Ελληνόφωνους που θέλουν να μάθουν Ισπανικά.
            Από αρχάριο σε μεσαίο επίπεδο, με τον δικό σου ρυθμό.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center animate-slideUp">
            <Link to="/learn">
              <Button size="lg" variant="primary">
                Ξεκίνα τώρα →
              </Button>
            </Link>
            {completedChapters > 0 && (
              <Link to="/progress">
                <Button size="lg" variant="outline" className="!border-white/30 !text-white hover:!bg-white/10">
                  Η πρόοδός μου
                </Button>
              </Link>
            )}
          </div>
        </div>
      </section>

      {/* Progress Summary */}
      {totalChapters > 0 && !loading && (
        <section className="max-w-6xl mx-auto px-4 -mt-6 md:-mt-8 relative z-10">
          <Card hover={false} className="bg-white/95 backdrop-blur">
            <div className="flex flex-col sm:flex-row items-center gap-4">
              <div className="flex-1 w-full">
                <h3 className="text-sm font-medium text-secondary/60 mb-1">Η πρόοδός σου</h3>
                <ProgressBar value={completedChapters} max={totalChapters} size="lg" />
              </div>
              <div className="text-center sm:text-right flex-shrink-0">
                <p className="text-3xl font-bold text-secondary">{completedChapters}/{totalChapters}</p>
                <p className="text-sm text-secondary/60">κεφάλαια</p>
              </div>
            </div>
          </Card>
        </section>
      )}

      {/* Continue Learning */}
      {nextChapter && !loading && (
        <section className="max-w-6xl mx-auto px-4 pt-8">
          <Card hover={false} className="bg-gradient-to-r from-primary/5 to-primary/10 border-primary/20">
            <div className="flex flex-col sm:flex-row items-center gap-4">
              <div className="text-4xl">🚀</div>
              <div className="flex-1 text-center sm:text-left">
                <p className="text-sm font-medium text-primary mb-0.5">Συνέχισε από εκεί που σταμάτησες</p>
                <p className="font-bold text-secondary">
                  Κεφάλαιο {nextChapter.order_index}: {nextChapter.title_greek}
                </p>
                <p className="text-xs text-secondary/50 italic">{nextChapter.title_spanish}</p>
              </div>
              <Link to={`/learn/${nextChapter.id}`}>
                <Button variant="primary" size="sm">Συνέχεια →</Button>
              </Link>
            </div>
          </Card>
        </section>
      )}

      {/* CTA Cards */}
      <section className="max-w-6xl mx-auto px-4 py-10 md:py-16">
        <div className="grid md:grid-cols-2 gap-6 md:gap-8">
          <Card className="text-center group">
            <div className="text-5xl mb-4 group-hover:scale-110 transition-transform">📚</div>
            <h2 className="text-2xl font-bold text-secondary mb-2">Μαθήματα</h2>
            <p className="text-secondary/70 mb-6">
              Ξεκίνα από την αρχή και προχώρα με τον ρυθμό σου.
              Δομημένα κεφάλαια από A1 έως B1.
            </p>
            <Link to="/learn">
              <Button variant="primary" size="md">Πάμε →</Button>
            </Link>
          </Card>

          <Card className="text-center group">
            <div className="text-5xl mb-4 group-hover:scale-110 transition-transform">📝</div>
            <h2 className="text-2xl font-bold text-secondary mb-2">Εξετάσεις</h2>
            <p className="text-secondary/70 mb-6">
              Δοκίμασε τις γνώσεις σου σε κάθε κεφάλαιο.
              Άμεση βαθμολόγηση και ανατροφοδότηση.
            </p>
            <Link to="/learn">
              <Button variant="secondary" size="md">Εξέταση →</Button>
            </Link>
          </Card>
        </div>
      </section>

      {/* Features */}
      <section className="max-w-6xl mx-auto px-4 pb-12 md:pb-16">
        <h2 className="text-xl md:text-2xl font-bold text-center text-secondary mb-8 md:mb-10">Γιατί αυτή η πλατφόρμα;</h2>
        <div className="grid sm:grid-cols-3 gap-4 md:gap-6">
          {[
            { icon: '🎯', title: 'Δομημένη Μάθηση', desc: '15 κεφάλαια από αρχάριο έως μεσαίο επίπεδο' },
            { icon: '🇬🇷', title: 'Στα Ελληνικά', desc: 'Όλες οι εξηγήσεις και οδηγίες στα Ελληνικά' },
            { icon: '📊', title: 'Παρακολούθηση', desc: 'Η πρόοδός σου αποθηκεύεται αυτόματα' },
          ].map((feature) => (
            <Card key={feature.title} className="text-center">
              <div className="text-4xl mb-3">{feature.icon}</div>
              <h3 className="font-bold text-secondary mb-1">{feature.title}</h3>
              <p className="text-sm text-secondary/60">{feature.desc}</p>
            </Card>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-secondary text-white/70 py-6 md:py-8">
        <div className="max-w-6xl mx-auto px-4 text-center text-sm">
          <p>Aprende Español — Πλατφόρμα εκμάθησης Ισπανικών για Ελληνόφωνους</p>
          <p className="mt-1">Σχολικό project © 2026</p>
        </div>
      </footer>
    </div>
  );
}
