from django.urls import path
from .views import PasswordCheckView

urlpatterns = [
    path('check-password/', PasswordCheckView.as_view(), name='check-password'),
]
