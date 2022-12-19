from django.urls import re_path
from . import views
from . import lookups

app_name = 'demoWeb'

urlpatterns = [
# Lookup
    re_path(r'^lookup_mainDishes/$', lookups.LookupMainDishes.as_view(), name='lookup_mainDishes'),
    re_path(r'^lookup_dessertDishes/$', lookups.LookupDessertDishes.as_view(), name='lookup_dessertDishes'),

# start
    re_path(r'^$', views.Start.as_view(), name='start'),
]