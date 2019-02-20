from django.urls import include, path
from rest_framework import routers
from . import views
from courses.views import CourseViewSet

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.DepartmentList.as_view(), name='departments'),
    path('courses/', views.CourseList.as_view(), name='courses'),
    path('courses/<course_department>/', views.CourseDepartmentList.as_view()),
    path('students/', views.StudentList.as_view(), name='students'),     
    path('professors/', views.ProfList.as_view(), name='professors'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
