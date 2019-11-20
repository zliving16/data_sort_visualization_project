from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.inputdata),
    url(r'^radix$', views.radixpage),
    url(r'^quicksort$', views.quickSort),
    url(r'^merge$', views.merge),
    url(r'^gravitySort$', views.gravitySort),
    url(r'^countSort$', views.countpage),
    url(r'^heapSort$', views.heapPage),
    url(r'^bogo$', views.bogoPage),
    url(r'^cocktail$', views.cocktailPage),
    url(r'^selection$', views.selectionPage),
    url(r'^bubble$', views.bubblePage),
    url(r'^quicksort/process$', views.quickSortProcess),
    url(r'^radix/process$', views.radixprocess),
    url(r'^merge/process$', views.mergeprocess),
    url(r'^gravitySort/process$', views.gravityProcess),
    url(r'^count/process$', views.countProcess),
    url(r'^heap/process$', views.heapProcess),
    url(r'^bogo/process$', views.bogoProcess),
    url(r'^selection/process$', views.selectionProcess),
    url(r'^cocktail/process$', views.cocktailProcess),
    url(r'^bubble/process$', views.bubbleProcess),
    url(r'^route/process$', views.routeProcess),
    url(r'^test$', views.colortest),
]
