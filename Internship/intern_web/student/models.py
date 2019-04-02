from django.db import models


#this is amount of job & internship model


class amount (models.Model):
    job=models.IntegerField()
    intern=models.IntegerField()
    company=models.IntegerField()
    city=models.IntegerField()

# this is Student all post model


class Stu_post(models.Model):
    Posting_title = models.CharField(max_length=100)
    slug = models.SlugField()
    Internship_discription = models.TextField()
    Location = models.CharField(max_length=50)
    job_type = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.CharField(max_length=50)

    def __str__(self):
        return self.Posting_title
