# Django Blog Project

A full-featured blog web application built with **Python** and **Django**, created by following the [Python Django - The Practical Guide](https://www.udemy.com/course/python-django-the-practical-guide/) course.

This project starts from the basics of Django and evolves into a production-ready blog, with personal customizations, styling, and additional features beyond the course material.

---

## 📚 About the Course

**"Python Django - The Practical Guide"** is a comprehensive course that covers:

- **Django Fundamentals:** Projects, apps, URLs, views, requests, responses
- **Templates & Static Files:** Rendering dynamic HTML, using Django Template Language, managing CSS/JS/images
- **Data & Models:** Database models, migrations, Django admin panel
- **Database Relationships:** One-to-many, one-to-one, many-to-many
- **Forms & User Input:** Handling submissions, validation, built-in form classes
- **Class-Based Views:** `TemplateView`, `ListView`, `DetailView`
- **File Uploads:** User-uploaded files and images
- **Sessions:** Features like "Read Later" lists
- **Deployment:** Preparing a Django project for production

---

## ✨ Project Features

**Core from the Course:**

- CRUD (Create, Read, Update, Delete) blog posts
- Homepage with latest posts
- All Posts page listing every blog post
- Post Detail pages with dynamic URLs
- Author & Tag support
- User comments
- File/Image uploads for posts
- "Read Later" session-based functionality
- Django Admin customization
- Class-Based Views for cleaner logic
- Deployment readiness

**Personal Additions:**

- 🎨 Custom styling & responsive design
- 📝 Extra blog features (to be revealed)
- ⚡ UX improvements & optimizations
- Planned: custom search functionality, rich text editor

---

## 🛠 Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS (custom), Django Template Language
- **Database:** SQLite (development), PostgreSQL (production)
- **Deployment-ready:** Static/media file handling, environment variables
- **IDE:** Visual Studio Code

---

## 🚀 Setup & Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/django-blog.git
cd django-blog
```

2. Create & activate a virtual environment:

```
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Apply database migrations:

```
python manage.py migrate
```

5. Create a superuser:

```
python manage.py createsuperuser
```

6. Run the development server:

```
python manage.py runserver
Visit: http://127.0.0.1:8000/
```

---

## Course Progress Checklist

This checklist helps track progress through the main sections of the course.

- [ ] **Section 1: Introduction**
- [ ] **Section 2: Course Setup**
- [ ] **Section 3: URLs & Views**
- [ ] **Section 4: Templates & Static Files**
- [ ] **Section 5: Course Project: Building a Blog (Initial Phase)**
- [ ] **Section 6: Data, Models & Databases**
- [ ] **Section 7: The Admin Site**
- [ ] **Section 8: Data Relationships (One-to-Many, Many-to-Many)**
- [ ] **Section 9: Course Project: Adding Models**
- [ ] **Section 10: Working with Forms**
- [ ] **Section 11: Class-Based Views**
- [ ] **Section 12: File Uploads**
- [ ] **Section 13: Sessions**
- [ ] **Section 14: Course Project: Comments & "Read Later"**
- [ ] **Section 15: Deploying the Website**
- [ ] **Section 16: Course Summary & Example Project**
- [ ] **Section 17: Course Roundup**

---

## 📦 Features Roadmap

- Basic post creation and display
- Comments section
- Tag system
- Admin customization
- User authentication (login, signup)
- Search functionality
- Pagination
- Dark mode support

---

## 🧠 Learning Goals

By completing this project, I aim to:

- Gain deep understanding of Django’s architecture (URLs, views, templates, models)
- Master database relationships in Django
- Work with forms, file uploads, and session data
- Prepare and deploy a Django app to production
- Apply my own creativity to enhance the course’s base project

---

## 📜 License

This project is for learning purposes.  
You are free to explore, fork, and adapt, but please respect the Udemy course’s original material and instructor’s content.

---

## 🙏 Credits

**Course:** _Python Django - The Practical Guide_  
**Instructor:** Maximilian Schwarzmüller (Udemy)  
**Additional improvements & customizations by:** [Your Name]
