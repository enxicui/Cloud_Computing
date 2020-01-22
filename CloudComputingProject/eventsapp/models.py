from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    event_name = models.CharField(max_length=200)
    event_description = models.TextField()
    location = models.CharField(max_length=200, default='Dublin')
    event_date = models.DateTimeField()
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_description
    #  From https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



