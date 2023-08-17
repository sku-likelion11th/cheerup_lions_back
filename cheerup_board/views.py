from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
import requests
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .models import PhotoPost, Comment, Message
from django.urls import reverse_lazy, reverse
from user_count import views

# Create your views here.
# api 호출용 함수
def get_api(url):
	response = requests.get(url)

	if response.status_code == 200:
		return response.json()
	else:
		return None

# 랜덤 닉네임 api https://nickname.hwanmoo.kr/?format=json&count=1
def test(request):
	anonymous_name = get_api("https://nickname.hwanmoo.kr/?format=json&count=1")
	print(anonymous_name["words"][0])
	return HttpResponse("<h1>Hi</h1>")


def main_page(request):
	return views.Counter(request)

#---------------------------------------- Board CRUD
class create_board(CreateView):
	model = PhotoPost
	fields = ['author', 'anony_password', 'photo', 'hook_text' ,'content']
	template_name = 'cheerup_board/board_create.html' # where to show

	def get_success_url(self):
		return reverse('board:board_list')
	# it goes to board_list url (app_name:name)


class update_board(UpdateView):
	model = PhotoPost
	fields = ['author', 'anony_password', 'photo', 'hook_text' ,'content']
	template_name = 'cheerup_board/board_update.html' # same with all models => leave the current data and make them edit

	def get_success_url(self):
		return reverse('board:board_list')


def delete_board(request, pk): # have to make the password confirmation
    post = get_object_or_404(PhotoPost, pk=pk)
    post.delete()
    return redirect(reverse('board:board_list'))


class board_list(ListView):
	model = PhotoPost
	context_object_name = 'board' 
	template_name = 'cheerup_board/board_list.html'
# {% for post in board %} use like this in the template


class board_detail(DetailView):
    model = PhotoPost
    template_name = 'cheerup_board/board_detail.html'
    
    def get_object(self, queryset=None):
        id = self.kwargs['pk']
        return PhotoPost.objects.get(id=id)
    


#---------------------------------------- comment CRUD

class create_comment(CreateView):
	model = Comment
	fields = ['author', 'anony_password', 'content']
	template_name = 'cheerup_board/comment_create.html'

	def get_success_url(self):
		return reverse('board:board_list')
	# it goes to board_list url (app_name:name)


class update_comment(UpdateView):
	model = Comment
	fields = ['author', 'anony_password', 'content']
	template_name = 'cheerup_board/comment_update.html'

	def get_success_url(self):
		return reverse('board:board_list')


def delete_comment(request, pk): # have to make the password confirmation
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect(reverse('board:board_list'))


# don't use list view on comment, it appeared in PhotoPost detail view
# class comment_list(ListView):
# 	model = PhotoPost
# 	context_object_name = 'board' 
# 	template_name = 'cheerup_board/board_list.html'
# {% for post in board %} use like this in the template


# don't use detail view on comment
# class board_detail(DetailView):
#     model = PhotoPost
#     template_name = 'cheerup_board/board_detail.html'
    
#     def get_object(self, queryset=None):
#         id = self.kwargs['id']
#         return PhotoPost.objects.get(id=id)
    


#---------------------------------------- message CRUD
class create_message(CreateView):
	model = Message
	fields = ['author', 'anony_password', 'content']
	template_name = 'cheerup_board/message_create.html'

	def get_success_url(self):
		return reverse('board:message_list')
	# it goes to message_list url (app_name:name)


class update_message(UpdateView):
	model = Message
	fields = ['author', 'anony_password', 'content']
	template_name = 'cheerup_board/message_update.html'

	def get_success_url(self):
		return reverse('board:message_list')


def delete_message(request, pk): # have to make the password confirmation
    message = get_object_or_404(Message, pk=pk)
    message.delete()
    return redirect(reverse('board:message_list'))


class message_list(ListView):
	model = Message
	context_object_name = 'messages' 
	template_name = 'cheerup_board/message_list.html'
# {% for message in messages %} use like this in the template


# don't use detail view on message
# class board_message(DetailView):
#     model = PhotoPost
#     template_name = 'cheerup_board/board_detail.html'
    
#     def get_object(self, queryset=None):
#         id = self.kwargs['id']
#         return PhotoPost.objects.get(id=id)