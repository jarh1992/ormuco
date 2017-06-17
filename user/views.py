from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import User


def index(request):
	resp = ''
	if request.method == 'POST':
		try:
			name = request.POST.get('name')
			if validName(name):
				col = request.POST.get('col')
				anim = request.POST.get('ani')
				if User.objects.filter(name=name).exists() == False:
					user = User()
					user.name = name.lower()
					user.f_color = col
					user.f_animal = anim
					user.save()
					resp = 'User saved successfully'
				else:
					resp = 'Error: Existing User'
			else:
				resp = "There are invalid characters in the name"
		except Exception:
			resp = "Sorry, we're having errors"

	template = loader.get_template('index.html')
	context = {
		'resp': resp,
	}
	return HttpResponse(template.render(context, request))

def validName(name):
	for c in name:
		if not c.isalpha() and not c.isspace():
			return False
	return True
