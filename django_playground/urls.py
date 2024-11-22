from django.contrib import admin
from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Home page
    path('about/', views.about_us, name='about_us'),  # About Us page
]
