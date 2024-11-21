
from django.urls import path
from calculator.views import pasta_view, buter_view, omlet_view, menu_view

urlpatterns = [
    path('omlet/', omlet_view, name='omlet'),
    path('pasta/', pasta_view, name='pasta'),
    path('buter/', buter_view, name='buter'),
    path('', menu_view, name='menu'),
]
