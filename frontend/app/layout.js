import './globals.css';
import Navbar from '../components/Navbar/Navbar';
import Footer from '../components/Footer/Footer';

export const metadata = {
  title: 'Student Performance Predictor',
  description: 'Predict student scores using ML',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div className="page-container">
          <Navbar />
          <main className="content-wrap">{children}</main>
          <Footer />
        </div>
      </body>
    </html>
  );
}
