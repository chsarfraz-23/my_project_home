from django.db import models
from django.contrib.auth.models import User, AbstractUser
import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    phone_number = models.CharField(max_length=12, unique=True, auto_created=False, null=True)
    id_card_number = models.CharField(max_length=13, unique=True, blank=True, auto_created=False)
    bank_account_number = models.CharField(max_length=30, unique=True, null=True, blank=True)


class Universty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=400, unique=True)
    registration_number = models.CharField(max_length=300)
    students = models.CharField(max_length=100000)
    teacher = models.CharField(max_length=10000, null=True, blank=True)
    ranking = models.CharField(max_length=200, null=True, blank=True)
    departments = models.CharField(max_length=300)
    labs = models.CharField(max_length=300, null=True, blank=True)
    area = models.CharField(max_length=300, null=True, blank=True)


class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    user = models.ForeignKey(Universty, on_delete=models.CASCADE, related_name='school')
    school_name = models.CharField(max_length=100, unique=True)
    obtained_marks = models.CharField(max_length=100)
    total_marks = models.CharField(max_length=100)


class AffiliateColleges(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    universty = models.ForeignKey(Universty, on_delete=models.CASCADE, related_name='affiliation')
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    ranking = models.CharField(max_length=200)


class Industries(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    universty = models.ForeignKey(Universty, on_delete=models.CASCADE, related_name='industry_connection')
    affiliated = models.ForeignKey(AffiliateColleges, on_delete=models.CASCADE,
                                   related_name='affiliated_college_industries')
    name = models.CharField(max_length=1000)
    sector = models.CharField(max_length=400)
    requirenment = models.CharField(max_length=300)


class College(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    user = models.ForeignKey(Universty, on_delete=models.CASCADE, related_name='college')
    students = models.CharField(max_length=300)
    marks = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300)


class Departments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    department = models.OneToOneField(Universty, on_delete=models.CASCADE, related_name='fee')
    name = models.CharField(max_length=300, unique=True)
    merit = models.CharField(max_length=400)
    seats = models.CharField(max_length=400)


class Fee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name="fee")
    image = models.ImageField(upload_to='fee_structure', unique=True)
    department = models.CharField(max_length=300)
    group = models.CharField(max_length=200)


class TestModel(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
