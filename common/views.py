import sys
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, Http404
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Choices


def home(request):
    # return HttpResponse("Home Page..........")
    return render(request, 'SQANow_home.html')


def about(request):
    # return HttpResponse('Hello from Home About......')
    return render(request, 'about.html')


# class CityListView(ListView):
#     model = City
#     #form_class = CityForm
#     context_object_name = 'city'


# class CityCreateView(CreateView):
#     model = City
#     template_name = 'common/city_add.html'
#     form_class = CityForm
#     # fields = ('name', 'city', 'country', 'state')
#     success_url = reverse_lazy('city_add')


# class CityUpdateView(UpdateView):
#     model = City
#     fields = ('name', 'city', 'country', 'state')
#     success_url = reverse_lazy('city_list')


# def load_states(request):
#     country_id = request.GET.get('country')
#     states = State.objects.filter(country_id=country_id).order_by('name')
#     return render(request, 'common/city_dropdown_list_options.html', {'states': states})


def get_ChoicesId():
    qs = Choices.objects.all()
    print(len(qs))
    return qs[0].id


get_ChoicesId()


# def load_cities(request):
#     country_id = request.GET.get('country')
#     cities = City.objects.filter(country_id=country_id).order_by('name')
#     return render(request, 'dev/city_list.html', {'cities': cities})
