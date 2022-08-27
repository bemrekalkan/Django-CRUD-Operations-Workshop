from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=50)
    number = models.IntegerField()
    mobile = models.IntegerField()
    email = models.EmailField(max_length=254)

    GENDER =(
        ("1", "Female"),
        ("2", "Male"),
        ("3", "Other"),
        ("4", "Prefer Not Say"),
    )

    gender = models.CharField( max_length=50, choices=GENDER)

    PATH = (
        ("1","Full Stack"),
        ("2", "Data Science"),
        ("3", "DevOps"),
        ("4", "AWS"),
        ("5", "ITF")
    )

    path = models.CharField(max_length=50, choices=PATH)

    def __str__(self):
            return self.fullname