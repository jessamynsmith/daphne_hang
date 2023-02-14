from django.urls import path

from . import views


urlpatterns = [
    path('api/v1/good/', views.good, name='good'),
    path('api/v1/hang/', views.hang, name='hang'),
]
