import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="hero">
      <h1>🎓 Welcome to EduPredict</h1>
      <p>Predict your exam score using smart machine learning!</p>
      <Link href="/predict">🚀 Try the Predictor</Link>
    </main>
  );
}
