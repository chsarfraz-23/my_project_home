from rest_framework import serializers

from new.models import KollaTesting


class KollaSerializer(serializers.ModelSerializer):
    class Meta:
        model = KollaTesting
        fields = "__all__"
