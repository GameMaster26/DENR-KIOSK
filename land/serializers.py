from rest_framework import serializers
from .models import LandClassificationApplication

class LandClassificationApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandClassificationApplication
        fields = ['full_name', 'address', 'number_of_trees', 'reason_for_cutting', 'documents', 'status', 'remarks', 'last_updated']
