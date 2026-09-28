import uuid

from django.contrib.auth.models import User
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=False)
    ended_at = models.DateTimeField(blank=True, null=True)
    starred_by = models.ManyToManyField(
        User, related_name="starred_experience", blank=True
    )

    class Meta:
        permissions = [
            ("can_star_experience", "Can star or like an experience card"),
            ("can_add_experience", "Can add an experience card"),
            ("can_delete_experience", "Can delete an experience card"),
            ("can_change_experience", "Can change information on an experience card"),
        ]

    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model):
    EDUCATION_CHOICES = [
        ('elementary', 'Elementary School'),
        ('junior', 'Junior High School'),
        ('senior', 'Senior High School'),
        ('college', 'College'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school_name = models.CharField(max_length=255)
    grade = models.CharField(max_length=20, choices=EDUCATION_CHOICES, default='college')
    started_at = models.DateTimeField(auto_now_add=False)
    ended_at = models.DateTimeField(blank=True, null=True)
    starred_by = models.ManyToManyField(
        User, related_name="starred_education", blank=True
    )

    class Meta:
        permissions = [
            ("can_star_education", "Can star or like an education card"),
            ("can_add_education", "Can add an education card"),
            ("can_delete_education", "Can delete an education card"),
            ("can_change_education", "Can change information on an education card"),
        ]

    def __str__(self):
        return self.school_name
    
    @property
    def is_ongoing(self):
        return self.ended_at is None