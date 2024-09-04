from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User

from myapp.models import School, Universty, AffiliateColleges, College, Industries, Departments, Fee, UserProfile, \
    TestModel

admin.site.register(UserProfile)
admin.site.register(School)
admin.site.register(College)
admin.site.register(Universty)
admin.site.register(Industries)
admin.site.register(AffiliateColleges)
admin.site.register(Departments)
admin.site.register(Fee)
admin.site.register(TestModel)
