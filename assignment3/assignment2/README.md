## Summary of the project

### Django Project Setup:

A Django project named degree_checklist was created.
An app within the project named degree_checklist was established to handle curriculum-related functionalities.
 
 ### Django Models:

Models were created in models.py to represent the entities defined in the ERD.
Models included DegreeProgram and Course with relevant fields and relationships.

### Django Admin Panel:

The Django Admin was configured to allow easy management of records using the Admin interface.
Instances of models were added through the Admin to represent the Bachelor of Business Administration in Computer Information Systems program.
### User-Facing Forms:

User-facing forms were created to enable users to interact with and manage curriculum aspects.
Views and templates were developed to handle form rendering and submission.
6. URL Routing:

URL patterns were defined in urls.py to map to the views responsible for rendering user-facing forms.
URLs for degree programs and courses were configured to access the respective views.
### Sorting Functionality:

Sorting functionality was implemented in the model_list view.
The view dynamically handled sorting based on different fields, including numeric sorting for fields like TotalCredits.
### Debugging and Troubleshooting:

Debug statements were added to the view to identify issues in sorting and data retrieval.
Templates were updated to display data and sorting links correctly.
### User Interface (HTML Templates):

HTML templates (model_list.html) were created to render the user interface for the model list views.
Templates included dynamic titles, sorting links, and lists of model instances.

## Execution command

1. Download the zip file and unzip it
2. cd /assignment3/assignment2
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver

## Instruction for Django admin 
Admin is accessible using http://127.0.0.1:8000/admin/ and all the required models are available as shown below

![Image] (https://github.com/vigneshkennady/CIDM6325-assignments/blob/main/assignment3/assignment2/Django_admin_degree_checklst.png)

Using Django admin records are loaded as highlighted below

For example - degreeProgram are added using DJangoadmin as highlighted below

![Image] (https://github.com/vigneshkennady/CIDM6325-assignments/blob/main/assignment3/assignment2/Django_admin_degree_checklst.png)

All the models are loaded with sample data as highlighted below


Model_list view has been created to view the degree program list and course list as highlighted below

#### Degree program list view
![Image] (https://github.com/vigneshkennady/CIDM6325-assignments/blob/main/assignment3/assignment2/Django_admin_degree_checklst.png)

#### course list view
![Image] (https://github.com/vigneshkennady/CIDM6325-assignments/blob/main/assignment3/assignment2/Django_admin_degree_checklst.png)
