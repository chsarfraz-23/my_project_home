# import pytest
# from django.contrib.auth.models import User
# from rest_framework.test import APIClient
# from myapp.models import College, Universty, School, AffiliateColleges, Industries, Departments, Fee
#
# @pytest.fixture
# def api_client():
#     yield APIClient()
#
#
# @pytest.fixture
# def fx_user():
#     return User.objects.create(username="Sarfraz", password="123123")
#
#
# @pytest.fixture
# def fx_universty():
#     return Universty.objects.create(name="IUB", registration_number=10101, students=10000,
#                                     teacher=1000, ranking=100, departments=100, labs=1000,
#                                     area=10000)
#
#
# @pytest.fixture
# def fx_college(universty):
#     return College.objects.create(user_id=universty.id, students=100, marks=100, name="Punjab college jahanian")
#
#
# @pytest.fixture
# def fx_school(user):
#     return School.objects.create(user_id=user.id, school_name="Govt High school ", obtained_marks=1000,
#                                  total_marks=1100)
#
#
# @pytest.fixture
# def fx_affiliate_college(universty):
#     return AffiliateColleges.objects.create(universty_id=universty.id, name="Punjab College ", location=30,
#                                             ranking=1000)
#
#
# @pytest.fixture
# def fx_industries(universty):
#     Industries.objects.create(universty_id=universty.id, affiliated="IUB", name="Systems", sector="IT",
#                               requirenment="Bachelor Of Science")
#
#
# @pytest.fixture
# def fx_departments(universty):
#     return Departments.objects.create(department_id=universty.id, name=universty.name,
#                                       merit=70, seats=100)
#
#
# @pytest.fixture
# def fx_fee(department):
#     return Fee.objects.create(department_id=department.id, image="file:///C:/Users/nadeem/Desktop/adventure.webp",
#                               department="Computing", group="1st")
