from django.db import models


# Create your models here.
class Film(models.Model):
    film_name = models.CharField(max_length=50)
    film_description = models.TextField()
    year = models.IntegerField()
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)

    def __str__(self):
        return self.film_name


class Actor(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year = models.DateField()

    def __str__(self):
        return self.name + " " + self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
