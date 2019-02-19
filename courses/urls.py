from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.DepartmentList.as_view(), name='departments'),
    path('courses/', views.CourseList.as_view(), name='courses'),
    path('courses/<course_department>/', views.CourseDepartmentList.as_view()),
    path('students/', views.StudentList.as_view(), name='students'),     
    path('professors/', views.ProfList.as_view(), name='professors'),
]
