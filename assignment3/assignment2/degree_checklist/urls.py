# urls.py in your app (e.g., degree_checklist)

from django.urls import path
from .views import create_course,create_degree_program,degree_program_list

urlpatterns = [
    path('create_degree_program/', create_degree_program, name='create_degree_program'),
    path('create_course/', create_course, name='create_course'),
    path('degree_program_list/', degree_program_list, name='degree_program_list'),

    # Add other URLs as needed
]

#