from django.urls import path
from . import views


app_name = "board"
urlpatterns = [
	path('', views.test),
    
    path('board/create/', views.create_board.as_view(), name='board_create'),
	path('board/update/<int:id>/', views.update_board.as_view(), name='board_update'),
	path('board/delete/<int:id>/', views.delete_board.as_view(), name='board_delete'),
    path('board/list/', views.board_list.as_view(), name='board_list'), # show all photo
    path('board/list/<int:id>/', views.board_detail.as_view(), name='board_detail'), # show detail of photo object
    
	path('comment/create/', views.create_comment.as_view(), name='comment_create'),
	path('comment/update/<int:id>/', views.update_comment.as_view(), name='comment_update'),
	path('comment/delete/<int:id>/', views.delete_comment.as_view(), name='comment_delete'),

	path('message/create/', views.create_message.as_view(), name='message_create'),
	path('message/update/<int:id>/', views.update_message.as_view(), name='message_update'),
	path('message/delete/<int:id>/', views.delete_message.as_view(), name='message_delete'),
    path('message/list/', views.message_list.as_view(), name='message_list'), # show all photo

]