# Fromvill Website

A premium, futuristic Next.js landing website for **Fromvill — AI • Research • Innovation**.

## Install dependencies

```bash
npm install
```

## Run locally

```bash
npm run dev
```

Open `http://localhost:3000`.

## Build

```bash
npm run build
```

## Deploy on Vercel

1. Push this repository to GitHub, GitLab, or Bitbucket.
2. Import the repository in Vercel.
3. Keep the default Next.js settings.
4. Click **Deploy**.

## Connect custom domain fromvill.com

1. In Vercel, open the project settings.
2. Go to **Domains** and add `fromvill.com` and `www.fromvill.com`.
3. Update DNS at your domain registrar using the records Vercel provides.
4. Wait for DNS propagation and SSL provisioning.

## Brand asset notes

- The website uses only the text-based `/public/logo.svg` asset for the logo, favicon, and social preview references.
- Binary image assets such as PNG, JPG, JPEG, WEBP, ICO, and uploaded image files are intentionally excluded from this change.
- Update WhatsApp, LinkedIn, GitHub, portfolio, and testimonials in `components/site.tsx`.
