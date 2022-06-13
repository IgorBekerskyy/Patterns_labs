from rest_framework import serializers

from jira_lab.models.caretaker import Caretaker


class CaretakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caretaker
        fields = '__all__'
