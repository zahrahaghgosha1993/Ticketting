from django.contrib.auth import get_user_model
from django.db import models

from ticket import constant

AUTH_USER = get_user_model()


class Ticket(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=700, null=True, blank=True)
    status = models.CharField(choices=constant.STATUS_CHOOSE,max_length=20)
    user = models.ForeignKey(AUTH_USER,
                             on_delete=models.CASCADE, )
