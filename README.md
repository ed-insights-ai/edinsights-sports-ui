# EDInsights Sports UI

Next.js 14 web application for the EDInsights higher education athletics analytics platform.

## Prerequisites

- Node.js 20+
- npm 10+
- Docker (optional, for containerized development)

## Getting Started

### Local Development

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Docker Development

```bash
docker compose up --build
```

The app runs at [http://localhost:3000](http://localhost:3000) with hot reload via volume mounts.

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS v3 with custom brand colors
- **Components**: shadcn/ui (Button, Card, Input, Label, Navigation Menu, Sheet, Toast, Avatar, Dropdown Menu)
- **Icons**: Lucide React

## Project Structure

```
src/
├── app/
│   ├── about/page.tsx      # About page
│   ├── dashboard/page.tsx  # Dashboard page
│   ├── login/page.tsx      # Sign in page
│   ├── signup/page.tsx     # Sign up page
│   ├── globals.css         # Global styles with CSS variables
│   ├── layout.tsx          # Root layout with Header & Footer
│   ├── not-found.tsx       # Custom 404 page
│   └── page.tsx            # Home page
├── components/
│   ├── ui/                 # shadcn/ui components
│   ├── Header.tsx          # Site header with navigation
│   └── Footer.tsx          # Site footer
└── lib/
    └── utils.ts            # Utility functions (cn)
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint
