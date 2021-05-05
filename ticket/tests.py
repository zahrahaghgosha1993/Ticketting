from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_mommy import mommy

from ticket.models import IssueType


class IssueTest(APITestCase):
    fixtures = ["fixture_data/issue_type.json", ]

    def setUp(self):
        self.auth_user = get_user_model()
        self.user = mommy.make(self.auth_user, username='test_user')
        self.client.force_authenticate(self.user)

    def test_create_issue(self):
        data = {'summary': 'test_create_issue', 'description': "test_description",
                'issue_type': IssueType.objects.get(id=10007).id}
        url = reverse('list_create_issue')
        response = self.client.post(url, data=data, format='json',)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_issue_with_problem_in_jira_service(self):
        data = {'summary': 'test_create_issue', 'description': "test_description",
                'issue_type': IssueType.objects.get(id=10007).id}
        url = reverse('list_create_issue')
        response = self.client.post(url, data=data, format='json',)
        self.assertEqual(response.status_code, 503)


