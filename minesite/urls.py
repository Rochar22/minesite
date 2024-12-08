from django.contrib import admin
from django.urls import path, include
from mineapp.views import get_user, title_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', get_user),
    path('', title_page),
    path('api/', include('mineapp.urls')),
]

