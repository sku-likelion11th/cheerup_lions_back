from .models import Counter
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta
from django.urls import reverse


# just use this module for user count
def user_count(request):

	try:
		user = Counter.objects.get(date=timezone.now())
	except Counter.DoesNotExist:
		user = Counter.objects.create(count=0, date=timezone.now())

	if request.COOKIES.get('visited') == 'yes':
		return render(request, 'cheerup_board/index.html')  # have to naming 'main' page , ex) path('/index', views.hi, name='main)
	else:
		key = 'visited'
		value = 'yes'
		now = datetime.now()
		end_of_day = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
		expire = end_of_day.strftime('%a, %d %b %Y %H:%M:%S GMT')

		res = render(request, 'cheerup_board/index.html')
		res.set_cookie(key, value=value, expires=expire)
		user.count += 1
		user.save()
  
		return res