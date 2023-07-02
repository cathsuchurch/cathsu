from django.db import models

# Create your models here.


class Document(models.Model):
    document_name = models.CharField(max_length=255)
    document_image = models.ImageField(upload_to="document_image")

    def __str__(self):
        return self.document_name


class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        # ('O', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active Member'),
        ('Affiliate', 'Affiliate Member'),
        ('Patron', 'Patron/Patronessess'),
    ]

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.PositiveIntegerField()
    house_number = models.CharField(max_length=255)
    hometown = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateField()
    profile_image = models.ImageField(upload_to='profile_images')
    previous_school = models.CharField(max_length=255)
    current_school = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    date_of_joining = models.DateField()
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.surname}'

