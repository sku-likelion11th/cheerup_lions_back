from django.urls import path
from . import views


app_name = "board"
urlpatterns = [
	path('', views.test),
    path('board/', views.board_list.as_view(), name='list'), # show all photo
    path('board/<int:id>/', views.board_detail.as_view(), name='detail'), # show detail of photo object
    
]