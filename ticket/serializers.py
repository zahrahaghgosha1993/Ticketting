from rest_framework import serializers

from ticket.models import Ticket


class CreateIssueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['summary', 'description', 'status', 'issue_type']

    def create(self, validated_data):
        validated_data['user'] = self.context['user']
        ticket = Ticket.objects.create(**validated_data)
        return ticket


class ListIssueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['summary', 'description', 'status', 'issue_type']
