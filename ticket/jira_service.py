from django.conf import settings

import requests


def create_issue(summary, description, issuetype, project_key):
    response = requests.post(
        "{}{}".format(
            settings.JIRA_BASE_API_URL,
            'issue/'
        ),
        json={
                "fields": {
                    "project":
                        {
                            "key": project_key
                        },
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

