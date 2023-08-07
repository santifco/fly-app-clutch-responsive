# fly/urls.py
from django.urls import path

from .views import homePageView
from . import views
from django.contrib.auth import views as auth_views
from django.db import models
from fly.views import * 

urlpatterns = [
    path("", homePageView, name="home"),
    path('base',views.base,name='base'),
    #path('talles_table',talles_table.as_view(),name='talles_table'),
    path('linktree',views.linktree,name='linktree'),
    path('linktree_soccer',views.linktree_soccer,name='linktree_soccer'),
    path('linktree_basketball_menu',views.linktree_basketball_menu,name='linktree_basketball_menu'),
    path('linktree_basketball_pedidos',views.linktree_basketball_pedidos,name='linktree_basketball_pedidos'),
    path('linktree_tenis',views.linktree_tenis,name='linktree_tenis'),
    path('linktree_urban',views.linktree_urban,name='linktree_urban'),
    path('linktree_genero',views.linktree_genero,name='linktree_genero'),
    path('linktree_urban_women',views.linktree_urban_women,name='linktree_urban_women'),
    path('linktree_volley',views.linktree_volley,name='linktree_volley'),
    path('calculator',views.calculator,name='calculator'),
    path('seguimiento',views.seguimiento,name='segiumiento'),
    path('calculator_mayorista',views.calculator_mayorista,name='calculator_mayorista'),
]

