from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateIssue.as_view(), name='list_create_issue'),
    path('test/', views.Test.as_view(), name='test'),

]
