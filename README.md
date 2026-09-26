# Md. Mehedi Hasan — AI & ML Researcher Portfolio

> Personal portfolio of **Md. Mehedi Hasan**, AI & ML Researcher at Dhaka International University.  
> Live at 👉 **[mdmehedihasan.onrender.com](https://mdmehedihasan.onrender.com)**  
> Custom domain: **[www.mdmehedihasan.us](https://www.mdmehedihasan.us)**

---

## 🖥️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Django 5.1 (Python 3.12+) |
| **Frontend** | Vanilla HTML · CSS · JavaScript |
| **Fonts** | Inter + JetBrains Mono (Google Fonts) |
| **Static Files** | WhiteNoise 6 |
| **Database** | SQLite (dev) · PostgreSQL (prod) |
| **Deployment** | Render.com (gunicorn) |
| **Version Control** | Git · GitHub |

---

## ✨ Features

- **Silicon Valley AI Lab** design — glassmorphism, spotlight hover cards, frosted glass navbar
- Fully responsive — desktop, tablet, mobile
- **Dark / Light mode** toggle with smooth transitions
- Animated skill marquee strips
- Tabbed publications viewer (Accepted · Under Review · Ongoing)
- BibTeX copy modal for each publication
- Interactive contact form (opens email client)
- Live status ticker bar
- Scroll-reveal animations
- Particle canvas background
- **Ambient SVG motifs** — SEM path diagrams, loss function equations, model pipelines
- JSON-LD structured data for SEO
- Open Graph + Twitter Card meta tags
- vCard (`.vcf`) download button
- Back-to-top button + scroll progress bar

---

## 🗂️ Project Structure

```
portfolio_django/
├── core/
│   ├── fixtures/
│   │   └── initial_data.json    # Seed data for DB
│   ├── migrations/              # Django migrations
│   ├── templates/
│   │   └── core/
│   │       └── index.html       # Main portfolio template
│   ├── models.py                # Profile, Publication, Project, Skill, Award …
│   ├── views.py                 # index view (DB-optional, graceful fallback)
│   └── admin.py                 # Django admin config
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   ├── css/
│   │   └── portfolio.css        # Complete design system
│   ├── js/
│   │   └── portfolio.js         # Animations, tabs, modal, vCard, contact form
│   └── images/                  # Profile photo, favicons
├── build.sh                     # Render build script
├── requirements.txt
└── manage.py
```

---

## 🚀 Local Development

### 1. Clone the repo
```bash
git clone https://github.com/meetmehedi/mdmehedihasan.git
cd mdmehedihasan
```

### 2. Create & activate virtual environment
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations & load seed data
```bash
python manage.py migrate
python manage.py loaddata core/fixtures/initial_data.json
```

### 5. Start the dev server
```bash
python manage.py runserver
```

Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser.

---

## ☁️ Deployment (Render)

The project is pre-configured for **[Render.com](https://render.com)** free tier.

| Setting | Value |
|---|---|
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn portfolio.wsgi:application` |
| **Environment** | Python 3 |

### Environment Variables (set in Render dashboard)

| Variable | Value |
|---|---|
| `DEBUG` | `False` |
| `DATABASE_URL` | *(optional — SQLite used if not set)* |
| `SECRET_KEY` | *(generate a random key)* |

> **Note:** The site renders fully without a database — all content is hardcoded in the HTML template. The DB layer is purely optional for the Django Admin CMS.

---

## 📬 Connect

| Platform | Link |
|---|---|
| 🌐 Website | [www.mdmehedihasan.us](https://www.mdmehedihasan.us) |
| 💼 LinkedIn | [linkedin.com/in/meetmehedi](https://www.linkedin.com/in/meetmehedi) |
| 🐙 GitHub | [github.com/meetmehedi](https://github.com/meetmehedi) |
| 📊 Kaggle | [kaggle.com/meetmehedi](https://www.kaggle.com/meetmehedi) |
| 🔬 ORCID | [0009-0006-1427-8769](https://orcid.org/0009-0006-1427-8769) |
| 📧 Email | meetmehedi1@gmail.com |

---

## 📄 License

© 2026 Md. Mehedi Hasan. All rights reserved.  
This portfolio is open-source for reference — please do not copy the design or content directly.
