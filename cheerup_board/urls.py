from django.urls import path
from . import views


app_name = "board"
urlpatterns = [
	path('', views.test),
    
    path('board/create/', views.create_board.as_view(), name='board_create'),
	path('board/update/<int:pk>/', views.update_board.as_view(), name='board_update'),
	path('board/delete/<int:pk>/', views.delete_board, name='board_delete'),
    path('board/list/', views.board_list.as_view(), name='board_list'),
    path('board/list/<int:pk>/', views.board_detail.as_view(), name='board_detail'),
    
	path('comment/create/', views.create_comment.as_view(), name='comment_create'),
	path('comment/update/<int:pk>/', views.update_comment.as_view(), name='comment_update'),
	path('comment/delete/<int:pk>/', views.delete_comment, name='comment_delete'),

	path('message/create/', views.create_message.as_view(), name='message_create'),
	path('message/update/<int:pk>/', views.update_message.as_view(), name='message_update'),
	path('message/delete/<int:pk>/', views.delete_message, name='message_delete'),
    path('message/list/', views.message_list.as_view(), name='message_list'), 
    
]