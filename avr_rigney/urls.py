from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('LightModule', views.LightView)
app_name = 'avr_rigney'
urlpatterns = [
  path('rest/',include(router.urls)),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('presets/', views.presetsPage, name='presetsPage'),
  path('settings/', views.settingsPage, name='settingsPage'),
  path('json/', views.get_lights, name='users')
]
