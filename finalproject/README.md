Project Description: Degree Checklist Management System

## Table of Contents
1. [Introduction](#Introduction)
2. [Features](#Features)
3. [User Interaction](#User-Interaction)
4. [Installation](#Installation)
5. [Running the Application](#Running-the-Application)
6. [Usage](#Usage)
7. [Testing](#Testing)
8. [Code Quality](#Code-Quality)



## Introduction

The Degree Checklist Management System is a comprehensive web application designed to streamline the management of degree programs, courses, and student enrollments within an academic institution. The system provides a user-friendly interface for administrators, faculty, and students to efficiently handle degree program creation, course management, and student enrollment tracking. It leverages the Django framework for backend development, ensuring robustness and scalability, and integrates the Django Rest Framework for API functionality.

## Features

Degree Program Management: The system allows administrators to effortlessly create, edit, and view degree programs. Each program includes details such as program name, total credits, and the department to which it belongs. Administrators can also associate core requirements and degree-specific requirements with each program.

### Department Management: 
Departments are an integral part of the system, and administrators can manage department details seamlessly. Each department is associated with multiple degree programs, facilitating efficient organization and navigation.

### Course Management: 
The system supports the creation and management of individual courses, including details such as course name, credits, department association, and optional linkage to a specific degree program. This feature enables academic staff to maintain an up-to-date course catalog.

### Enrollment Tracking: 
The system tracks student enrollments in degree programs, providing a clear overview of which students are enrolled in specific programs. This feature is particularly useful for academic advisors and department heads to monitor student progress.

### Requirement Associations: 
Core requirements and degree-specific requirements are associated with degree programs, allowing administrators to define the academic criteria that students must fulfill. This ensures that students are aware of the essential courses needed for degree completion.

### API Integration: 
The system includes a robust API, enabling third-party applications to access and interact with degree program, course, and student enrollment data. This facilitates integration with other systems within the academic institution.

## User Interaction

### Administrators: 
Have access to the entire system, allowing them to create and manage degree programs, departments, courses, and requirements. They can also view student enrollments and generate reports for academic analysis.

### Faculty: 
Can utilize the system to access and update course information, view student enrollments, and collaborate with administrators on program and department management.

### Students: 
Have limited access to view their degree program, enrolled courses, and academic requirements. This allows them to track their progress and plan their academic journey effectively.

## API Endpoints

The system provides a set of API endpoints for external integration, allowing other systems to fetch and update data related to degree programs, courses, and student enrollments. This ensures flexibility and interoperability with other institutional systems.

## Future Enhancements

The Degree Checklist Management System is designed to evolve, with future enhancements planned to include features such as automated notifications for degree progress, integration with learning management systems, and enhanced reporting capabilities.

## Conclusion

In conclusion, the Degree Checklist Management System offers a robust and user-friendly solution for academic institutions to efficiently manage degree programs, courses, and student enrollments. With its modular design, comprehensive features, and API integration, the system is poised to enhance the academic administration process and contribute to the overall success of students and faculty.


## Installation

To install the necessary dependencies, use the following commands:

```bash
pip install -r requirements.txt
```

## Running the Application
To run the application locally, follow these steps:
1. Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate 
```

2. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
3. Create a superuser account (for admin access):
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials to access the admin interface.

## Usage
The application provides interfaces for administrators, faculty, and students. Here are the main features:

### Admin Interface: 
Manage degree programs, courses, departments, and student enrollments.
URL: http://127.0.0.1:8000/degree_checklist/create_degree_program/
Screenshot:
![Image](screenshot1.jpg)
![Image](screenshot2.jpg)

URL: http://127.0.0.1:8000/degree_checklist/create_degree_program/
Screenshot:
![Image](screenshot3.jpg)
![Image](screenshot4.jpg)

### Faculty Interface: 
Access and update course information, view student enrollments.
URL: http://127.0.0.1:8000/degree_checklist/course_list/
![Image](screenshot6.jpg)
UR:http://127.0.0.1:8000/degree_checklist/degree_program_list/
![Image](screenshot5.jpg)
URL:http://127.0.0.1:8000/degree_checklist/degree_detail/1/
![Image](screenshot7.jpg)

### Student Interface: 
View degree program details, enrolled courses, and academic requirements.
URL:http://127.0.0.1:8000/degree_checklist/students/1/

![Image](screenshot8.jpg)

### API Endpoints
The application provides API endpoints for external integration. 
Here are some key endpoints:
/api/degree/<program_id>/: Retrieve details about a specific degree program.

Screenshot:
![Image](screenshot9.jpg)

## Testing
The project includes test cases for essential models. To run the tests, use the following command:

```bash
python manage.py test
```

## Code Quality
The code structure is well-organized, and Django best practices are followed. The code includes comments and docstrings where necessary.

## Future Enhancements
We have plans to enhance the application with the following features:

Automated notifications for degree progress.
Integration with learning management systems.
Enhanced reporting capabilities.