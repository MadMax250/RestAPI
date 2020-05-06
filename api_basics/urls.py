
from django.urls import path
from .views import article_list, artical_detail


urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>/', artical_detail)

]
