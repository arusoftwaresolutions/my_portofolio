# 🚀 Araya Haftu's Portfolio Website

A modern, animated, responsive fullstack developer portfolio website built with HTML, CSS, JavaScript, and Django.

## ✨ Features

- **Modern Design**: Clean, professional dark theme with gradient accents
- **Responsive Layout**: Optimized for desktop, tablet, and mobile devices
- **Smooth Animations**: CSS animations and JavaScript interactions
- **Contact Form**: Django backend with email notifications
- **Interactive Elements**: Hover effects, smooth scrolling, and dynamic content

## 🛠️ Tech Stack

### Frontend
- HTML5, CSS3, JavaScript (ES6+)
- Font Awesome Icons, Google Fonts (Inter)
- AOS (Animate On Scroll) Library

### Backend
- Django 4.2.7
- PostgreSQL (production) / SQLite (development)
- SMTP Email Backend
- WhiteNoise for static files

## 📁 Project Structure

```
myportofolio/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── Procfile                  # Render deployment configuration
├── render.yaml              # Render service configuration
├── .gitignore               # Git ignore rules
├── env.example              # Environment variables template
├── README.md                # This file
├── DEPLOYMENT_GUIDE.md      # Step-by-step deployment guide
├── portfolio_backend/        # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Production-ready settings
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── contact/                 # Contact form app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/               # HTML templates
│   └── index.html
└── static/                  # Static files
    ├── styles.css
    ├── script.js
    └── IMG_4431.JPG
```

## 🚀 Quick Start

### Local Development

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations**
   ```bash
   python manage.py migrate
   ```

3. **Start development server**
   ```bash
   python manage.py runserver
   ```

4. **Access the website**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

### Production Deployment

Follow the detailed guide in `DEPLOYMENT_GUIDE.md` to deploy on Render.

## 📧 Email Configuration

The contact form sends emails to `arayahaftu1229@gmail.com`. Configure email settings using environment variables:

```bash
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=arayahaftu1229@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## 🎨 Customization

### Personal Information
Edit `templates/index.html` to update:
- Your name and title
- About section content
- Project links and descriptions
- Contact information
- Certifications

### Styling
Modify `static/styles.css` for custom styling and colors.

## 📱 Responsive Design

- **Mobile**: < 480px
- **Tablet**: 480px - 768px
- **Desktop**: > 768px

## 🔧 Development Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test
```

## 🚀 Deployment

This project is configured for deployment on Koyeb with:
- PostgreSQL database
- WhiteNoise for static files
- Environment variable configuration
- Production-ready settings

See `KOYEB_DEPLOYMENT_GUIDE.md` for complete deployment instructions.

## 📄 License

This project is created for Araya Haftu's portfolio.

## 👨‍💻 Author

**Araya Haftu**
- Email: arayahaftu1229@gmail.com
- LinkedIn: [linkedin.com/in/araya21](https://linkedin.com/in/araya21)
- GitHub: [github.com/arusoftwaresolutions](https://github.com/arusoftwaresolutions)
- Twitter: [@ARAYA122123](https://twitter.com/ARAYA122123)

---

Built with ❤️ by Araya Haftu