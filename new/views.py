from rest_framework import viewsets

from new.models import KollaTesting
from new.serializers import KollaSerializer


class KollaView(viewsets.ModelViewSet):
    serializer_class = KollaSerializer
    queryset = KollaTesting.objects.all()

