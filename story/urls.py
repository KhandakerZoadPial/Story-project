from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('create_male_story', views.male_story, name='male_story')
]
