from django.db import models

from django.db import models
from django.utils import timezone

class RedditThread(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    created_utc = models.CharField(max_length=50)  # Store as a string
    url = models.URLField()

    def get_created_utc_datetime(self):
        # Convert the string timestamp to a datetime object
        return timezone.datetime.fromtimestamp(float(self.created_utc))
