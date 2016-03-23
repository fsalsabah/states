from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from main.models import State, City, StateCapital
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View 
from django.views.generic.list import ListView  
from main.forms import CitySearchForm, CityEditForm, CreateCityForm
from django.views.generic.detail import DetailView
from django.template import RequestContext
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
def city_delete(request, pk):
	City.objects.get(pk=pk).delete()
	return redirect('/city_search/')


def city_create(request):
	request_context = RequestContext(request)
	context = {}

	if request.method == 'POST':
		form = CreateCityForm(request.POST)
		context['form'] = form

		if form.is_valid():
			form.save()
			return render_to_response('city_create.html', context, context_instance=request_context)

		else:
			context['valid'] = form.errors
			return render_to_response('city_create.html', context, context_instance=request_context)

	else:
		form = CreateCityForm()
		context['form'] = form

		return render_to_response('city_create.html', context, context_instance=request_context)


class CityDetailView(DetailView):  
	model = City
	template_name = "city_detail.html"
	context_object_name = "city"


class StatesListView(ListView):  
	model = State
	template_name = "state_list.html"
	context_object_name = "state_list"


def city_search(request):
	request_context = RequestContext(request)

	context = {}

	if request.method== 'POST':
		form = CitySearchForm(request.POST)
		context['form'] = form

		if form.is_valid():
			name = '%s' % form.cleaned_data['name']
			state = form.cleaned_data['state']

			context['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)
			return render_to_response('city_search.html', context, context_instance=request_context)
		else:
			context['valid'] = form.errors
			return render_to_response( "city_search.html", context, context_instance=request_context )

	else:
		form = CitySearchForm()
		context["form"] = form

		return render_to_response( "city_search.html", context, context_instance=request_context )



def template_view(request):
	
	context = {}

	states = State.objects.all()

	context['states'] = states
	for state in states:
		print state
		print state.city_set.all()

	return render(request, 'state_list.html', context)
	

def state_detail(request, name):
	
	context = {}

	state = State.objects.get(name=name)

	return HttpResponse(state)

def state_list (request):
	states = State.objects.all()

	state_list = []

	for state in states:
		state_list.append("<a href='/state_detail/%s'>%s </a> <br>" % (state.name, state.name))

	return HttpResponse(state_list)


def city_edit(request, pk):

	context = {}

	city = City.objects.get(pk=pk)

	form = CityEditForm(request.POST or None, instance=city)

	context['city'] = city
	context['form'] = form

	if form.is_valid():
		form.save()
		return redirect('/state_list/')
	return render_to_response('city_edit.html', context, context_instance=RequestContext(request))


def contact_view(request):

	context = {}

	if request.method == 'POST':
		form = ContactForm(request.POST)
		context['form'] = form
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']
			message = form.cleaned_data['message']

			send_mail('STATES SITE MESSAGE FROM %s' % name,
					  message,
					  email,
					  [settings.EMAIL_HOST_USER],
					  fail_silently=False
					  )
			context['message'] = "email sent"
		else:
			context['message'] = form.errors
	elif request.method == 'GET':
		form = ContactForm()
		context['form'] = form

	return render_to_response('contact_view.html', context, context_instance=RequestContext(request))