from . import views
from django.urls import path


urlpatterns=[
    path('',views.calculator,name='calculator'),
    path('fun',views.fun,name='fun')
]
