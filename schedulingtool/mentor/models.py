from django.db import models
from django.contrib.auth import get_user_model #Django will find what model you are using
from datetime import datetime, timedelta

User = get_user_model()

event_category = (
    ("Flash", "Flash"),
    ("Plus", "Plus"),
    ("One Day Workshop", "One Day Workshop")
)

location_category = (
    ("Sydney", "Sydney"),
    ("Perth", "Perth"),
    ("Brisbane", "Brisbane")
)
# Create your models here.
class Event(models.Model):
    image=models.URLField(default="https://shecodes.com.au/wp-content/uploads/2020/02/Purple_no_circle.svg")
    event_type=models.CharField(max_length=200, null=True, choices= event_category)
    location=models.CharField(max_length=200, null=True, choices= location_category)
    description=models.TextField()
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=(datetime.now() + timedelta(days=30)))
    status= models.BooleanField(default=True)
    

