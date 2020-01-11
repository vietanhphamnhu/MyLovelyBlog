from django.contrib import admin
from django.urls import path 
from django.views.generic import TemplateView


urlpatterns = [
    path('cuongmax/', admin.site.urls),
    path('', TemplateView.as_view(template_name="theme/index.html")),

] 