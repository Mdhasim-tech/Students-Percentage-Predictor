import Link from 'next/link';

export default function Navbar() {
  return (
    <nav>
      <Link href="/" className="logo">
        📚 EduPredict
      </Link>
      <ul>
        <li><Link href="/">Home</Link></li>
        <li><Link href="/predict">Predict</Link></li>
      </ul>
    </nav>
  );
}
