from django.urls import path

from . import views
'''
Daniel Cummings
CST8333 Programming Language Research Project
'''

urlpatterns = [
    path('', views.index, name='index'),
    # path('table', views.table, name='table'),
]