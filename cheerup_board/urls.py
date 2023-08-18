from django.urls import path
from . import views


app_name = "board"
urlpatterns = [
    path('', views.main_page, name='main'),
    # path('mainpage/', views.index_page, name='main'),
    
    path('board/create/', views.create_board.as_view(), name='board_list'),
	path('board/update/<int:pk>/', views.update_board.as_view(), name='board_update'),
	path('board/delete/<int:pk>/', views.delete_board, name='board_delete'),
    
    path('board/list/<int:pk>/', views.board_detail.as_view(), name='board_detail'),
	path('comment/update/<int:pk>/', views.update_comment.as_view(), name='comment_update'),
	path('comment/delete/<int:pk>/', views.delete_comment, name='comment_delete'),

	path('message/update/<int:pk>/', views.update_message.as_view(), name='message_update'),
	path('message/delete/<int:pk>/', views.delete_message, name='message_delete'),
	path('message/list/', views.MessageView.as_view(), name='message_list'), 
	path('get_images/', views.get_image_list),
	path('get_messages/', views.get_message)
]