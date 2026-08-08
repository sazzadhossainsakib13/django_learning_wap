# 🎓 School Management Portal

A Django web application modeling academic administration, course registries, faculty directories, classroom logistics, and attendance tracking.

[![Python: 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Framework-Django-092E20.svg?logo=django)](https://www.djangoproject.com/)
[![Database: SQLite](https://img.shields.io/badge/Database-SQLite-003B57.svg?logo=sqlite)](https://www.sqlite.org/)

---

## Overview

The **School Management Portal** provides structured academic data management for educational institutions. It implements relational database models and dynamic Django template views to manage faculty records, student enrollment, academic departments, courses, examination schedules, classroom capacities, and daily attendance logs.

---

## Implemented Modules & Features

- **Faculty Directory (`TeacherModel`)**: Manage teacher profiles, institutional contact information, and email registries.
- **Student Information System (`StudentModel`)**: Track student identities, roll numbers, and age records.
- **Department Administration (`Dept`)**: Manage academic departments, department heads, and designated administrative offices.
- **Curriculum & Courses (`CourseModel`)**: Catalog courses with standardized course codes, titles, and credit allocations.
- **Examination Schedules (`ExamModel`)**: Manage exam dates and total marks tracking.
- **Classroom Logistics (`ClassroomModel`)**: Manage building locations, room identifiers, and seating capacities.
- **Attendance Records (`AttendanceModel`)**: Log student attendance statuses and session dates.

---

## Tech Stack

- **Backend**: Python 3, Django
- **Frontend**: Django Templates (HTML5, CSS3)
- **Database**: SQLite 3

---

## Project Structure

```text
django_learning_wap/
├── School_management/   # Root configuration, project settings, global views, and URL routing
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── student/             # Core academic data models and migrations
│   └── models.py
├── template/            # HTML templates for views (home, student, teacher, etc.)
├── db.sqlite3           # Local SQLite database
├── manage.py            # Django CLI management utility
└── README.md            # Documentation
```

---

## Installation & Local Setup

### Prerequisites
- Python 3.9+
- `pip`

### 1. Clone the Repository
```bash
git clone https://github.com/sazzadhossainsakib13/django_learning_wap.git
cd django_learning_wap
```

### 2. Set Up a Virtual Environment
```bash
# On Linux/macOS:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Database Setup & Run Server
```bash
python manage.py migrate
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.

---

## Route Overview

| Endpoint | View | Description |
| :--- | :--- | :--- |
| `/` | `home_page` | Institutional landing dashboard |
| `/teacher/` | `teacher_page` | Faculty registry and contact list |
| `/student/` | `student` | Enrolled student rosters and roll numbers |
| `/dept/` | `Dept_page` | Academic departments and department heads |
| `/course/` | `course_page` | Course catalog, codes, and credit hours |
| `/exam/` | `exam_page` | Examination dates and total marks |
| `/classroom/` | `classroom_page` | Campus buildings and room capacities |
| `/attendance/` | `attendance_page` | Daily student attendance logs |

---

## Author

**Sazzad Hossain Sakib**  
- GitHub: [@sazzadhossainsakib13](https://github.com/sazzadhossainsakib13)
