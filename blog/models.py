from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32, default="title")
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + self.last_name


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField
    star_nums = models.IntegerField

