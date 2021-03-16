from rest_framework import serializers
from rest_framework import permissions

from .models import Reduction

class ReductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reduction
        fields = '__all__'