# 🌐 Social Media Platform – Built with Django

Welcome to the **Social Media Platform**, a beginner-friendly yet feature-rich web application built using the Django framework. This project demonstrates how to build a basic social media experience where users can share updates, connect with others, and manage their profiles.

📁 **Project Repository:**  
🔗 [View on GitHub](https://github.com/RiteshPanchal279/ritesh_panchal_pythonCourse/tree/main/Final%20Project/social-media)

---

## 🧩 Features

- ✅ User registration and authentication
- 👤 Editable user profiles (profile picture and bio)
- 📰 News feed showing posts from followed users
- 📝 Create and delete posts
- ❤️ Like and unlike posts
- ➕ Follow and ➖ unfollow users
- 🔍 Search users by username
- 📱 Responsive, mobile-friendly UI using HTML/CSS

---

## 🚀 Getting Started

### ⚙️ Prerequisites

Make sure the following are installed:

- Python 3.6 or higher
- Django 3.2 or higher
- Git

### 📥 Installation

Clone the repository and set up the environment:

```bash
# Clone the project
git clone https://github.com/RiteshPanchal279/ritesh_panchal_pythonCourse.git
cd ritesh_panchal_pythonCourse/Final\ Project/social-media

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create an admin user (optional)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
