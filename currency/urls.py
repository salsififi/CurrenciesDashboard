from django.urls import path

from .views import dashboard

urlpatterns = [
    path('days=<int:days_range>&currencies=<str:currencies>', dashboard, name='home'),
]
