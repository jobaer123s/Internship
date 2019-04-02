from django.db import models
from django.forms.fields import DateField

# this is for craeting intern post model


class Post(models.Model):
    Posting_title = models.CharField(max_length=100)
    slug = models.SlugField()
    Internship_discription = models.TextField()
    Location = models.CharField(max_length=50)
    job_type = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.CharField(max_length=50)

    def __str__(self):
        return self.Posting_title


# this is for applying for intern  model


class Apply(models.Model):
    Expected_salery = models.IntegerField(blank=False)
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    nationality = models.CharField(max_length=30)
    contact = models.CharField(max_length=11)
    address = models.TextField()
    birth = models.DateField(max_length=30)

    def __str__(self):
        return self.email