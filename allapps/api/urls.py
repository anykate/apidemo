from django.urls import path
from . import views


app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/words/', views.WordListAPIView.as_view(),
         name='word_list_api_view'),
]
