from django.conf.urls import url
from . import views

#set the namespace
#app_name = 'my_app'
 
urlpatterns = [
   url('biology/', views.biology, name='biology'),
   url('physics/', views.physics, name='physics'),
   url('geometry/', views.geometry, name='geometry'),
   url('martial_arts/', views.martial_arts, name='martial_arts'),
   url('math/', views.math, name='math'),
]
