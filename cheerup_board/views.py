from django.http import HttpResponse
from django.shortcuts import render
import requests

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