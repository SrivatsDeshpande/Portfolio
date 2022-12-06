from django.db import models

# Create your models here.
class Work(models.Model):
    company = models.CharField(max_length = 150)
    designation = models.CharField(max_length = 150)
    from_date = models.DateField()
    to_date = models.DateField()
    description = models.TextField(max_length = 500)

    def __str__(self):
        return self

class Education(models.Model):
    course = models.CharField(max_length = 150)
    institution = models.CharField(max_length = 150)
    from_date = models.DateField()
    to_date = models.DateField()
    gpa = models.FloatField()

class Projects(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    tech = models.CharField(max_length = 150)
    learnings = models.CharField(max_length = 150)



        


