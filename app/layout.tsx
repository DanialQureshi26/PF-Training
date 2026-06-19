import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
const inter = Inter({ subsets: ['latin'], variable: '--font-inter' });
export const metadata: Metadata = {
  metadataBase: new URL('https://fromvill.com'),
  title: 'Fromvill | AI, Research & Development Solutions',
  description: 'Fromvill provides AI development, machine learning, chatbots, automation, research support, and modern web development services for businesses, researchers, and startups.',
  keywords: ['AI services','machine learning','chatbots','AI agents','computer vision','research support','web development','automation','Fromvill'],
  openGraph: { title: 'Fromvill | AI, Research & Development Solutions', description: 'AI development, machine learning, chatbots, automation, research support, and modern web development services.', url: 'https://fromvill.com', siteName: 'Fromvill', images: ['/logo.svg'], type: 'website' },
  icons: { icon: '/logo.svg', shortcut: '/logo.svg', apple: '/logo.svg' }
};
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en" className="scroll-smooth"><body className={`${inter.variable} font-sans antialiased`}>{children}</body></html>; }
