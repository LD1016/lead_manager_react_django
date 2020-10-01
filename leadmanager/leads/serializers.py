from leads.models import Lead
from rest_framework import serializers

# Make serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Lead
        fields = '__all__'