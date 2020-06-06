from django.db import models

# Create your models here.


class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
