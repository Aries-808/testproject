# Research Submission Application - README

## Overview
This Django application allows users to submit and manage research data, research papers, and theses. It provides an authentication system for users to register and login, and once authenticated, they can upload research materials and view others' submissions.

## Features
- **User Authentication**: Register and login functionality using Django's built-in authentication system.
- **Submit Research Data**: Users can upload research data associated with research papers.
- **Submit Research Papers**: Users can submit research papers, which can have associated data files.
- **Submit Theses**: Users can upload and manage their theses.
- **View Submissions**: All users can view a list of submitted theses and research papers. Detailed views are provided for individual submissions.

## Requirements
- Python 3.x
- Django 4.x or later

## Installation
1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open a browser and go to `http://127.0.0.1:8000/`.

## Application Structure

### `views.py`
- **`login_view`**: Handles user login using Django's `AuthenticationForm`. Redirects to the home page upon successful login.
- **`register`**: Handles user registration with `UserCreationForm`. After successful registration, it redirects to the login page.
- **`submit_research_data`**: Allows logged-in users to upload research data files associated with a research paper.
- **`submit_thesis`**: Handles submission of a thesis, associating it with the logged-in user.
- **`submit_research_paper`**: Handles submission of research papers, associating them with the logged-in user.
- **`index`**: Displays a list of all submitted theses and research papers.
- **`research_list`**: Lists all research papers.
- **`thesis_list`**: Lists all theses.
- **`research_details`**: Displays detailed information about a specific research paper, along with associated research data.
- **`thesis_details`**: Displays detailed information about a specific thesis.

### `models.py`
- **`Thesis`**: Represents a thesis, with a title, description, author (linked to `User`), and an associated file.
- **`ResearchPaper`**: Represents a research paper with a title, description, author (linked to `User`), and an associated file.
- **`ResearchData`**: Represents research data linked to a specific research paper, uploaded by the user who authored it.

## Templates
- **`login.html`**: Template for the login form.
- **`register.html`**: Template for the registration form.
- **`index.html`**: Home page template that displays the list of theses and research papers.
- **`submit_thesis.html`**: Template for submitting theses.
- **`submit_research_paper.html`**: Template for submitting research papers.
- **`submit_research_data.html`**: Template for submitting research data.
- **`research_list.html`**: Template for displaying all research papers.
- **`thesis_list.html`**: Template for displaying all theses.
- **`research_details.html`**: Template for displaying detailed information about a specific research paper.
- **`thesis_details.html`**: Template for displaying detailed information about a specific thesis.

## URL Routing
Ensure that the `urls.py` file is properly configured to route requests to the views in `views.py`. Example URL configuration might look like:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('submit_thesis/', views.submit_thesis, name='submit_thesis'),
    path('submit_research_paper/', views.submit_research_paper, name='submit_research_paper'),
    path('submit_research_data/', views.submit_research_data, name='submit_research_data'),
    path('research_list/', views.research_list, name='research_list'),
    path('thesis_list/', views.thesis_list, name='thesis_list'),
    path('research_details/<int:paper_id>/', views.research_details, name='research_details'),
    path('thesis_details/<int:thesis_id>/', views.thesis_details, name='thesis_details'),
]
```

## Usage
1. **Register** for an account using the registration form.
2. **Login** to access the submission features.
3. **Submit** research papers, theses, and associated data files.
4. **View** the submissions from other users on the home page.

## License
This project is licensed under the MIT License.

---

This `README` file serves as a basic guide to the structure and functionality of the Django application. Feel free to expand on it by adding details specific to your project setup, deployment instructions, or any other relevant information.
