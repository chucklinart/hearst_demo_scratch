from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.core.paginator import Paginator
from .models import Department, Course, Student, Prof

class DepartmentList(ListView):
    model = Department
    ordering = ('name', )
    template_name='departments.html'
    paginate_by = 20    
    queryset = Department.objects.all()
    context_object_name = 'department_list'

class CourseList(ListView):
    model = Course
    ordering = ('course_title', )
    template_name='courses.html'
    paginate_by = 20
    queryset = Course.objects.all()
    context_object_name = 'course_list'   

class CourseDepartmentList(ListView):
    template_name = 'course_department_list.html'
    def get_queryset(self):
        self.course_department = get_object_or_404(Department, name=self.kwargs['course_department'])
        return Course.objects.filter(course_department=self.course_department)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the department
        context['course_department'] = self.course_department
        return context
    context_object_name = 'courses_by_department'

class StudentList(ListView):
    model = Student
    ordering = ('last_name', )
    template_name='students.html'
    paginate_by = 50
    queryset = Student.objects.all()
    context_object_name = 'student_list'
    
class ProfList(ListView):
    model = Prof
    ordering = ('last_name', )
    template_name = 'professors.html'
    avatar = 'avatar'
    paginate_by = 10
    queryset = Prof.objects.all()
    context_object_name = 'prof_list'

def home(request):
    return render(request, 'home.html')

