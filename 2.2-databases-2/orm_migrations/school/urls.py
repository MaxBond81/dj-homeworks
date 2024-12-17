import debug_toolbar
from django.conf import settings
from django.urls import path, include
from school.views import students_list



urlpatterns = [
    path('', students_list, name='students'),

]
