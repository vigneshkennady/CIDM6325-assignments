# views.py

from django.shortcuts import render, redirect
from .forms import DegreeProgramForm, CourseForm,DegreeProgram

def create_degree_program(request):
    if request.method == 'POST':
        form = DegreeProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('degree_program_list')
    else:
        form = DegreeProgramForm()

    return render(request, 'create_degree_program.html', {'form': form})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('degree_program_list')
    else:
        form = CourseForm()

    return render(request, 'create_course.html', {'form': form})

def degree_program_list(request):
    degree_programs = DegreeProgram.objects.all()
    return render(request, 'degree_program_list.html', {'degree_programs': degree_programs})
