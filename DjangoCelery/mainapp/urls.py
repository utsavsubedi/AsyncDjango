from django.urls import path 
from . import views as mainapp_views


urlpatterns = [
    path('', mainapp_views.test, name = "test"),
]