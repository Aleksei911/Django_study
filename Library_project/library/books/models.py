from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publishing_house = models.CharField(max_length=60)
    year_of_publication = models.IntegerField()
    pages = models.IntegerField()
    binding = models.CharField(max_length=60)
    weight = models.CharField(max_length=6)
    age_restrictions = models.CharField(max_length=3)
    image = models.FileField(upload_to='img/')

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
