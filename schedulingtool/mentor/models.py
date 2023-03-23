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

level_category = (
    ("Junior", "Junior"),
    ("Industry", "Industry"),
    ("Lead", "Lead")
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
    

class Mentor(models.Model):
    first_name=models.CharField(max_length=50, null=True)
    last_name=models.CharField(max_length=50, null=True)
    email=models.EmailField()
    bio=models.TextField()
    image=models.URLField(default="https://shecodes.com.au/wp-content/uploads/2021/10/Screen-Shot-2021-12-07-at-12.00.01-pm-400x400.png")
    skills=models.CharField(max_length=500)
    level=models.CharField(max_length=200, null=True, choices= level_category)
    interview=models.BooleanField(default=False)
    offer=models.BooleanField(default=False)
    contract_sent=models.BooleanField(default=False)
    contract_return=models.BooleanField(default=False)
    onboarding_completed=models.BooleanField(default=False)
    feedback_sent=models.BooleanField(default=False)
    offboarding=models.BooleanField(default=False)
    events = models.ManyToManyField("Event",related_name="mentors",blank=True)
    