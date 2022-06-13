from rest_framework import serializers

from jira_lab.models.compensation import Compensation


class CompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compensation
        fields = '__all__'
