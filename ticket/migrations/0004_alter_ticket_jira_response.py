# Generated by Django 3.2 on 2021-05-02 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_ticket_jira_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='jira_response',
            field=models.JSONField(default={}),
        ),
    ]
