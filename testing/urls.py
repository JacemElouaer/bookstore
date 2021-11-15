from django.urls import path
from . import views

urlpatterns = [
    path('testhome/',  views.testhome),
    path('abouttest/',  views.abouttest),
    path('customer/',  views.customer),
    path('profile/',  views.profile),
]