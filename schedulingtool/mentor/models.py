from django.db import models
from django.contrib.auth import get_user_model #Django will find what model you are using
# from datetime import datetime, timedelta

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

class Tech_Stack(models.Model):

    name = models.CharField(max_length=300, unique=True)
    image = models.URLField(default="shorturl.at/lxP34")

    def __str__(self):
        return self.name
    
class Mentor(models.Model):

    first_name=models.CharField(max_length=50, null=True)
    last_name=models.CharField(max_length=50, null=True)
    email=models.EmailField()
    bio=models.TextField()
    image=models.URLField(default="https://shecodes.com.au/wp-content/uploads/2021/10/Screen-Shot-2021-12-07-at-12.00.01-pm-400x400.png")
    level=models.CharField(max_length=200, null=True, choices= level_category)
    location=models.CharField(max_length=200, null=True, choices= location_category)
    can_travel= models.BooleanField(default=False)
    mentor_tech_stack=models.ManyToManyField(Tech_Stack, related_name="tech_mentor")

    # class Meta:
    #     verbose_name = "mentor"
    #     verbose_name_plural = "mentors"

    def __str__(self):
        return f"{self.first_name}::{self.last_name}"
    

class Event(models.Model):

    title = models.CharField(max_length=300, unique=True)
    image=models.URLField(default="https://shecodes.com.au/wp-content/uploads/2020/02/Purple_no_circle.svg")
    event_type=models.CharField(max_length=200, null=True, choices= event_category)
    location=models.CharField(max_length=200, null=True, choices= location_category)
    description=models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status= models.BooleanField(default=True)
    
    mentors = models.ManyToManyField(Mentor,related_name="events", through="mentor.Onboarding")
    event_tech_stack=models.ManyToManyField(Tech_Stack, related_name="events_tech")

    def __str__(self):
        return self.title

# on_delete=models.PROTECT means forbid the deletion of the referenced object by raising ProtectedError. 
# To delete it you will have to delete all objects that reference it manually.
class Onboarding(models.Model):
    mentor = models.ForeignKey(Mentor,on_delete=models.CASCADE, related_name="onboardings", blank=True, null=True) #get list added as attribute
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)

    interview = models.BooleanField()
    offer = models.BooleanField()
    contract_sent = models.BooleanField()
    contract_return = models.BooleanField()
    onboarding_completed = models.BooleanField()
    feedback = models.BooleanField()
    offboarding = models.BooleanField()

    # interview = models.ForeignKey(User, on_delete=models.PROTECT, related_name="interview_user")
    # offer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="offer_user")
    # contract_sent = models.ForeignKey(User, on_delete=models.PROTECT, related_name="contract_sent_user")
    # contract_return = models.ForeignKey(User, on_delete=models.PROTECT, related_name="contract_return_user")
    # onboarding_completed = models.ForeignKey(User, on_delete=models.PROTECT, related_name="onboarding_completed_user")
    # feedback = models.ForeignKey(User, on_delete=models.PROTECT, related_name="feedback_user")
    # offboarding = models.ForeignKey(User, on_delete=models.PROTECT, related_name="offboarding_user")

    def __str__(self):
        return f"{self.event}::{self.mentor}"