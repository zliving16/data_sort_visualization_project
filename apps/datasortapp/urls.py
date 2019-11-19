from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.inputdata),
    url(r'^radix$', views.radixpage),
    url(r'^quicksort$', views.quickSort),
    url(r'^merge$', views.merge),
    url(r'^gravitySort$', views.gravitySort),
    url(r'^quicksort/process$', views.quickSortProcess),
    url(r'^radix/process$', views.radixprocess),
    url(r'^merge/process$', views.mergeprocess),
    url(r'^gravitySort/process$', views.gravityProcess),
]
