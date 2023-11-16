# degree_checklist/admin.py

from django.contrib import admin
from .models import Department, DegreeProgram, CoreRequirement, Course, DegreespecificRequirement, Student, EnrollsIn, BelongsTo, Requires, Includes, Has, IncludesDegreespecific

admin.site.register(Department)
admin.site.register(DegreeProgram)
admin.site.register(CoreRequirement)
admin.site.register(Course)
admin.site.register(DegreespecificRequirement)
admin.site.register(Student)
admin.site.register(EnrollsIn)
admin.site.register(BelongsTo)
admin.site.register(Requires)
admin.site.register(Includes)
admin.site.register(Has)
admin.site.register(IncludesDegreespecific)
