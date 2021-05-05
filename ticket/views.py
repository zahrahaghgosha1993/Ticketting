from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView

from ticket import jira_service
from ticket.exceptions import DefaultServerError
from ticket.models import Ticket
from ticket.serializers import ListIssueSerializers, CreateIssueSerializers
from ticketing import settings
from rest_framework.response import Response


class ListCreateIssue(ListCreateAPIView):

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListIssueSerializers
        elif self.request.method == 'POST':
            return CreateIssueSerializers

    def get_serializer_context(self):
        if self.request.method == 'POST':
            context = super().get_serializer_context()
            context["user"] = self.request.user
            return context

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data
        ticket = self.perform_create(serializer)
        try:
            response = jira_service.create_issue(
                summary=valid_data.get('summary'),
                description=valid_data.get('description'),
                issuetype=valid_data.get('issue_type').name,
                project_key=settings.PROJECT_KEY)
        except:
            ticket.jira_response = {
                "error": "DefaultServerError"
            }
            raise DefaultServerError

        ticket.jira_response = response.json()
        ticket.save()

        if response.status_code == 201:
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            raise DefaultServerError


class Test(APIView):

    def get(self, request, format=None):

        print("it works")
        return Response({"info": "works"})


