from django.db import models

# Create your models here.

class djangoClasses(models.Model):
    title = models.CharField(max_length=30, default="")
    CourseNumber = models.IntegerField()
    InstructorName = models.CharField(max_length=30, default="")
    Duration = models.FloatField()

    objects = models.Manager()

    # Returns title of djangoClasses instead of object name
    def __str__(self):
        return self.title
