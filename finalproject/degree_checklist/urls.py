# urls.py in your app (e.g., degree_checklist)

from django.urls import path
from .views import create_course,create_degree_program,degree_program_list,model_list,course_list,student_detail,degree_detail,api_degree_detail,DegreeDetailView

urlpatterns = [
    path('create_degree_program/', create_degree_program, name='create_degree_program'),
    path('create_course/', create_course, name='create_course'),
    path('degree_program_list/', degree_program_list, name='degree_program_list'),
    path('model_list/', model_list, name='model_list'),
    path('course_list/', course_list, name='course_list'),
    path('students/<int:student_id>/', student_detail, name='student_detail'),
    # path('degree_view/', degree_view, name='degree_view'),
    path('degree_detail/<int:program_id>/', degree_detail, name='degree_detail'),
    # path('degrees/<int:program_id>/', degree_view, name='degree_view'),
    path('api/degree/<int:program_id>/', DegreeDetailView.as_view(), name='degree-detail-api'),



]

#