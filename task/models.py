from django.db import models
from django.utils import timezone

# Create your models here.
#-auto_increment_id = models.AutoField(primary_key=True)

class task (models.Model):
    idtask = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    datedeadline = models.DateTimeField(null=True, blank=True)
    datecreate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

