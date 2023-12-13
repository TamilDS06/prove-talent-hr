from rest_framework import serializers
from versionOne.models import CandidateDirectory

class CandidatedirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateDirectory
        fields = '__all__'  # Include all fields in the serializer
