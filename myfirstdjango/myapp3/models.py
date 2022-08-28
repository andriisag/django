from django.db import models

from django.db import models

class MyApp(models.Model):
    name = models.CharField('Name', max_length = 200)
    surname = models.CharField('Surname', max_length = 200)
    age = models.BooleanField('Age', default=0)
    status = models.BooleanField('Status', default=True)

    def __str__(self):
        return self.name + " " + self.surname

class Sug(models.Model):
    name = models.CharField('Name', max_length = 200)
    sug = models.CharField('Suggestion', max_length = 200)

    def __str__(self):
        return self.name + " " + self.sug

class Meta:
    verbose_name = 'user'
    verbose_name_plural = 'users'
