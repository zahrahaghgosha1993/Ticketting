from django.conf import settings

import requests

from .exceptions import DefaultServerError


def create_issue(summary, description, issuetype, project_key):
    try:
        response = requests.post(
            "{}{}".format(
                settings.JIRA_BASE_API_URL,
                'issue/'
            ),
            json={
                "fields": {
                       "summary": summary,
                       "description": description,
                       "issuetype": {
                          "name": issuetype
                       }
                   }
            },
            headers=settings.JIRA_API_HEADERS
        )
        return response
    except Exception:
        raise DefaultServerError
