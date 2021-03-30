from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('all_cases/', views.login, name='all_cases'),
    path('help/', views.signup, name='help'),
    path('case/<name>', views.case_deatils, name='case_details'),
]