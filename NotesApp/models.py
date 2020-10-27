from django.db import models
from django.utils.timezone import now


class NotesApp(models.Model):
    title = models.CharField(max_length=100, default='Technology')
    content = models.TextField()
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now, blank=True)
