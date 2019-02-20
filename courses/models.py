from django.db import models
from django.utils.html import escape, mark_safe
from PIL import Image
from rest_framework import serializers

class Department(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)
    
class Course(models.Model):
    course_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='course_department')
    course_title = models.CharField(max_length=75)
    course_description = models.CharField(max_length=140)
    # make values available to Python API
    def __str__(self):
        return self.course_title

# demo RESTful API encpoint for Courses    
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('course_title', 'course_description')


class Student(models.Model):
    courses = models.ManyToManyField(Course, related_name='student_courses')
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    major = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='student_major')
    def __str_(self):
        return self.last_name

class Prof(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='prof_department', default=1)
    courses = models.ManyToManyField(Course, related_name='prof_courses')
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    avatar = models.ImageField(
        upload_to='avatars', 
        default='user_generic2_black.png',
        null=True,
        blank=True,
        editable=True,
        help_text="Prof Headshot",
        verbose_name="Headshot",
    )
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")

    def __unicode__(self):
        return "{0}".format(self.image)

    def __str_(self):
        return self.last_name

    def save(self):
        if not self.avatar:
            return            

        super(Prof, self).save()
        avatar = Image.open(self.avatar)
        (width, height) = avatar.size     
        size = ( 100, 100)
        avatar = avatar.resize(size, Image.ANTIALIAS)
        avatar.save(self.avatar.path)
