# Eventia Summit 2025 - Event Management & Conference Website

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

A premium, fully responsive frontend implementation for a modern event management and conference website. detailed features for attendees, speakers, and administrators.

## 🚀 Project Overview

**Eventia Summit 2025** is a comprehensive frontend solution designed to deliver a high-end user experience for conference management. It features a complete set of 10+ pages covering everything from landing pages and registration flows to user and admin dashboards.

The project emphasizes a "mobile-first" approach, modern aesthetics using Tailwind CSS, and global accessibility with built-in LTR/RTL toggle support.

## ✨ Key Features

- **Responsive Design**: Fully responsive layouts that adapt seamlessly from mobile to desktop.
- **Modern UI/UX**: Glassmorphism effects, smooth gradients, and micro-interactions.
- **RTL Support**: Full bi-directional support (Left-to-Right & Right-to-Left) with a single toggle.
- **Dynamic Interactions**:
  - Smooth scrolling and scroll-spy navigation.
  - Interactive tabs, accordions, and modals.
  - Custom JavaScript carousels and sliders.
  - Animated statistics counters.
- **Dark/Light Mode Elements**: Smart header adaptation based on scroll and page theme.
- **Mock Data Persistence**: `sessionStorage` usage for multi-step registration forms and RTL preferences.

## 🛠️ Technology Stack

- **Core**: Semantic HTML5
- **Styling**: Tailwind CSS (v3.4 via CDN)
- **Scripting**: Vanilla JavaScript (ES6+)
- **Icons**: FontAwesome 6
- **Fonts**: Google Fonts (Inter, Noto Sans)

> **Note**: This project utilizes Tailwind CSS via utility classes directly in HTML. No build step is required for development.

## 📂 Project Structure

```text
event-conference-website/
├── 📄 index.html             # Main Landing Page (Dark Theme)
├── 📄 index2.html            # Alternative Landing Page (Light Theme)
├── 📄 home2.html             # Variation of Home Page
├── 📄 event-details.html     # Detailed Event Info (Tabs: About, Venue, Speakers)
├── 📄 schedule.html          # Interactive Session Schedule with Filters
├── 📄 register.html          # Multi-step Registration Wizard
├── 📄 contact.html           # Contact Form & Info
├── 📄 login.html             # Authentication Page
├── 📄 user-dashboard.html    # Attendee Dashboard (My Schedule, Tickets)
├── 📄 admin-dashboard.html   # Admin Control Panel (Analytics, Management)
├── 📄 404.html               # Custom Error Page
├── 📄 coming-soon.html       # Pre-launch Countdown Page
├── 📂 assets/
│   └── 📂 images/            # Project assets and placeholders
└── 📂 js/
    ├── 📄 main.js            # Core application logic
    └── 📄 rtl-toggle.js      # Global RTL/LTR toggle handler
```

## 🚀 Getting Started

Since this is a static frontend project, no complex installation or build process is needed.

1.  **Clone or Download** the repository.
2.  **Open** the project folder.
3.  **Launch** `index.html` (or any other HTML file) directly in your modern web browser.

For the best experience, use a local development server (like Live Server in VS Code) to ensure all assets load correctly without CORS issues.

## 🔐 Demo Credentials

This project includes mock authentication flows. You can use the following credentials to simulate login scenarios:

| Role | Email | Password | Target Page |
| :--- | :--- | :--- | :--- |
| **User** | `user@event.com` | `user123` | `user-dashboard.html` |
| **Admin** | `admin@event.com` | `admin123` | `admin-dashboard.html` |

*Note: Authentication is simulated on the frontend. No real backend validation occurs.*

## 🎨 Pages Overview

1.  **Home (v1 & v2)**: Showcases the event with hero sections, speakers, stats, and testimonials.
2.  **Event Details**: comprehensive info using a clean tabbed layout.
3.  **Schedule**: Filterable agenda by track, speaker, or type.
4.  **Registration**: A progressive multi-step form with state persistence.
5.  **Dashboards**:
    *   **User**: Personal schedule management and ticket download.
    *   **Admin**: High-level overview, charts, and data tables.

## 📄 License

This project is created for educational and demonstration purposes.

---

*Built with ❤️ by [Your Name/Team]*
