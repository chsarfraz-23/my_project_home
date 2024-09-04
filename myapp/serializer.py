from django.db import transaction
from rest_framework import serializers
from myapp.models import School, Universty, College, AffiliateColleges, Industries, Departments, Fee, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'first_name', 'last_name', "email", 'is_active', 'is_staff',
                  'is_superuser', 'groups', 'phone_number', 'id_card_number', 'bank_account_number'
                  ]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class Affiliate(serializers.ModelSerializer):
    class Meta:
        model = AffiliateColleges
        fields = '__all__'


class IndustriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industries
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'


class UniverstySerializer(serializers.ModelSerializer):
    class Meta:
        model = Universty
        fields = "__all__"


class NestedSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(many=True, read_only=True)
    college = CollegeSerializer(many=True)
    universty = UniverstySerializer(many=True)

    class Meta:
        model = UserProfile
        fields = [
            'username', 'email', 'school', 'college', 'universty'
        ]


class DataByStringSerializer(serializers.ModelSerializer):
    school = serializers.StringRelatedField(many=True)
    college = serializers.StringRelatedField(many=True)
    universty = serializers.StringRelatedField(many=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'school', 'college', 'universty']


class DataByHyperLinkSerializer(serializers.ModelSerializer):
    school = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='school-detail')
    college = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='college-detail')
    universty = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='universty-detail')

    class Meta:
        model = UserProfile
        fields = [
            'username', 'email', 'school', 'college', 'universty'
        ]


class DataByHyperLinkIdentity(serializers.HyperlinkedModelSerializer):
    school = serializers.HyperlinkedIdentityField(view_name='school-detail')
    college = serializers.HyperlinkedIdentityField(view_name='college-detail')
    universty = serializers.HyperlinkedIdentityField(view_name='universty-detail')

    class Meta:
        model = UserProfile
        fields = [
            'username', 'email', 'school', 'college', 'universty'
        ]


class DataByPrimaryKeyRelated(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    college = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    universty = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'school', 'college', 'universty']


class DataBySlugRelated(serializers.ModelSerializer):
    school = serializers.SlugRelatedField(many=True, read_only=True, slug_field='school_name')
    college = serializers.SlugRelatedField(many=True, read_only=True, slug_field='colege_name')
    universty = serializers.SlugRelatedField(many=True, read_only=True, slug_field='universty_name')

    class Meta:
        model = UserProfile
        fields = [
            'username', 'email', 'school', 'college', 'universty']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'


class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'


class DepartmentNestedSerializer(serializers.ModelSerializer):
    fee = FeeSerializer(many=True, read_only=True)

    class Meta:
        model = Departments
        fields = '__all__'


class UniverstyNestedSerializer(serializers.ModelSerializer):
    affiliation = Affiliate(many=True)
    industry_connection = IndustriesSerializer(many=True)

    class Meta:
        model = Universty
        fields = [
            'name', 'registration_number', 'students', 'teacher', 'ranking', 'departments', 'labs', 'departments',
            'area', 'industry_connection', 'affiliation'
        ]
