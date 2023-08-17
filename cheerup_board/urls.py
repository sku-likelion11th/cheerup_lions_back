from django.urls import path
from . import views


app_name = "board"
urlpatterns = [
	path('', views.test),
    
    path('board/create/', views.create_board.as_view(), name='create'),
	path('board/update/<int:id>/', views.update_board.as_view(), name='update'),
	path('board/delete/<int:id>/', views.delete_board.as_view(), name='delete'),
    path('board/list/', views.board_list.as_view(), name='list'), # show all photo
    path('board/list/<int:id>/', views.board_detail.as_view(), name='detail'), # show detail of photo object
    
	path('comment/create/', views.create_board.as_view(), name='create'),
	path('comment/update/<int:id>/', views.update_board.as_view(), name='update'),
	path('comment/delete/<int:id>/', views.delete_board.as_view(), name='delete'),
    path('comment/list/', views.board_list.as_view(), name='list'), # show all photo
    path('comment/list/<int:id>/', views.board_detail.as_view(), name='detail'),
    
	path('message/create/', views.create_board.as_view(), name='create'),
	path('message/update/<int:id>/', views.update_board.as_view(), name='update'),
	path('message/delete/<int:id>/', views.delete_board.as_view(), name='delete'),
    path('message/list/', views.board_list.as_view(), name='list'), # show all photo
    path('message/list/<int:id>/', views.board_detail.as_view(), name='detail'),
    
]