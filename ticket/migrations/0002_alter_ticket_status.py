# Generated by Django 3.2 on 2021-05-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('sent', 'sent'), ('open', 'open'), ('answered', 'answered')], default='open', max_length=20),
        ),
    ]
