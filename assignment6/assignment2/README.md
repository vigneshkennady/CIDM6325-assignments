Summary:

The project is a Django-based degree checklist application designed to manage degree programs, courses, and related information. It includes models such as DegreeProgram, Department, CoreRequirement, Course, DegreespecificRequirement, Student, and relationship models like EnrollsIn, BelongsTo, Requires, Includes, Has, and IncludesDegreespecific.

Notably, the project incorporates the django-import-export library to enable seamless data import and export operations. This functionality is extended to the Django admin interface for the DegreeProgram model, allowing users to upload data files for bulk import or export dataset to files.

## Degree Checklist Application
### Overview
The Degree Checklist application is a web-based tool built on Django, designed to manage information related to degree programs, courses, and more. It includes a comprehensive set of models and relationships to cover various aspects of academic programs.

### Features
Degree Programs: Manage details about different degree programs, including program name, total credits, and department affiliation.

Courses: Keep track of various courses, including course name, credits, and associated department.

Departments: Store information about academic departments.

Requirements: Handle core requirements and degree-specific requirements.

Students: Manage student information and their enrollment in degree programs.

#### Import and Export Functionality
A key feature of this project is the integration of the django-import-export library, providing seamless import and export capabilities for data. The import/export functionality is specifically implemented for the DegreeProgram model within the Django admin interface.

#### Import Data
- Easily upload data files in various formats (CSV, Excel) through the Django admin interface.
- Bulk import degree program data, including program name, total credits, and department affiliation.
- Efficiently update and add new records to the database.

#### Export Data
- Export the dataset of degree programs to a downloadable file (CSV, Excel) through the Django admin interface.
- Generate reports or backups of degree program information with just a few clicks.

#### Getting Started
1. Clone the repository to your local machine.


`git clone https://github.com/your-username/degree-checklist.git`
2. Install dependencies.
pip install -r requirements.txt
3. Apply migrations.


python manage.py migrate
4. Create a superuser account.


python manage.py createsuperuser
5. Run the development server.


python manage.py runserver

Access the admin interface at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

Explore the Degree Programs section to utilize the import and export functionality as highlighted below

