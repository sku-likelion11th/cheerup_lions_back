from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .models import PhotoPost, Comment, Message
from django.urls import reverse_lazy, reverse

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


# have to make views each cheering, photo, message? idk
class create_board(CreateView):
	model = PhotoPost
	fields = ['author', 'anony_password', 'photo', 'hook_text' ,'content']
	template_name = ''

	def get_success_url(self):
		return reverse('board:list')
	# it goes to board/list url (app_name/name)


class update_board(UpdateView):
	model = PhotoPost
	fields = ['author', 'anony_password', 'photo', 'hook_text' ,'content']
	template_name = ''

	def get_success_url(self):
		return reverse('board:list')


class delete_board(DeleteView):
    model = PhotoPost
    template_name = ''
    success_url = reverse_lazy('board:list')


class board_list(ListView):
	model = PhotoPost
	context_object_name = 'board' 
	template_name = 'cheerup_board/board_list.html'
# {% for post in board %} use like this in the template

class board_detail(DetailView):
    model = PhotoPost
    template_name = 'cheerup_board/board_detail.html'
    
    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return PhotoPost.objects.get(id=id)