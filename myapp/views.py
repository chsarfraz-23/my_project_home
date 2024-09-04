from django.db.models import Prefetch
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from myapp import enum
from myapp.models import School, Universty, College, AffiliateColleges, Industries, Departments, Fee, UserProfile
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from myapp.serializer import (SchoolSerializer, CollegeSerializer, UniverstySerializer, UserSerializer,
                              DataByStringSerializer, DataByHyperLinkSerializer, DataByHyperLinkIdentity,
                              DataByPrimaryKeyRelated, DataBySlugRelated, NestedSerializer, Affiliate,
                              IndustriesSerializer,
                              UniverstyNestedSerializer, DepartmentSerializer, FeeSerializer, DepartmentNestedSerializer
                              )
from django.contrib.auth.models import Permission
from rest_framework_simplejwt.authentication import JWTAuthentication
from myapp.utils import validate_permission, user_in_group


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000


class UserView(CreateModelMixin, GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = UserProfile.objects.get_nearby(user)
        return queryset


class IndustriesView(viewsets.ModelViewSet):
    queryset = Industries.objects.all()
    serializer_class = IndustriesSerializer
    permission_classes = [IsAuthenticated]


class UniverstyNestedView(viewsets.ModelViewSet):
    queryset = Universty.objects.all()
    serializer_class = UniverstyNestedSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class AffiliationView(viewsets.ModelViewSet):
    queryset = AffiliateColleges.objects.all()
    serializer_class = Affiliate
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class NestedData(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = NestedSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    # pagination_class = LargeResultsSetPagination
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get_queryset(self):
        data = UserProfile.objects.prefetch_related(
            'groups',
            Prefetch(
                'user_permissions',
                queryset=Permission.objects.select_related('content_type').all())
        )
        return data

class SchoolView(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    permission_classes = [IsAuthenticated]


class CollegeView(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class UniverstyView(viewsets.ModelViewSet):
    queryset = Universty.objects.select_related('user').all()
    serializer_class = UniverstySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class GetDataS(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = DataByStringSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class GetDataH(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = DataByHyperLinkSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class GetDataHI(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = DataByHyperLinkIdentity
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class GetDataP(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = DataByPrimaryKeyRelated
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class GetDataSlug(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = DataBySlugRelated
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class DepartmentView(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class DepartmentNestedView(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentNestedSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class FeeView(viewsets.ModelViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
