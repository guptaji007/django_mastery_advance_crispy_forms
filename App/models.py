from django.db import models

SITUATION = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Dispproved', 'Dispproved'),
)

PERSONALITY = (
    # ('', 'Select a personality'),
    ('I am Outgoing', 'I am Outgoing'),
    ('I am sociable', 'I am sociable'),
    ('I am antisocial', 'I am antisocial'),
    ('I am discreet', 'I am discreet'),
    ('I am serious', 'I am serious'),
)

SMOKER = (
    ('1', 'Yes'),
    ('2', 'No'),
)

# Create your models here.
class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=20) # +91 9998887770
    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=10, choices=SMOKER, default="")
    email = models.EmailField(max_length=50)
    message = models.TextField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending') 

    def __str__(self):
        return self.firstname
    
    # Capitalize (First and Last Name)
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()