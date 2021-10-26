from django.shortcuts import render, redirect


# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Boat, Owner
from .forms import GearForm

def home(request):
  return HttpResponse('<h1> Boat Registry</h1>')

def about(request):
  return render(request, 'about.html')

def boats_index(request):
  boats = Boat.objects.all()
  return render(request, 'boats/index.html',{'boats': boats} )

def boats_detail(request, boat_id):
  boat = Boat.objects.get(id=boat_id)
  gear_form = GearForm()
  return render (request, 'boats/detail.html', {
    'boat':boat, 'gear_form': gear_form
  })

def add_gear(request, boat_id):
  form = GearForm(request.POST)
  if form.is_valid():
    new_gear = form.save(commit=False)
    new_gear.boat_id = boat_id
    new_gear.save()
  return redirect('detail', boat_id=boat_id)


class BoatList(ListView):
  model = Boat
  template_name = 'boats/index.html'

class BoatCreate(CreateView):
  model = Boat
  fields = ['name', 'registration_date', 'registration_number', 'comments']
  success_url='/boats/'

class BoatUpdate(UpdateView):
  model = Boat
  fields = ['registration_date', 'registration_number', 'comments']
  success_url='/boats/'

class BoatDelete(DeleteView):
  model = Boat
  success_url='/boats/'


class OwnerList(ListView):
  model = Owner

class OwnerDetail(DetailView):
   model = Owner

class OwnerCreate(CreateView):
  model = Owner
  fields = '__all__'

class OwnerUpdate(UpdateView):
  model = Owner
  fields = ['name']

class OwnerDelete(DeleteView):
  model = Owner
  success_url = '/owners/'

def assoc_owner(request, boat_id, owner_id):
  Boat.objects.get(id=boat_id).owners.add(owner_id)
  return redirect('detail', boat_id=boat_id)

def unassoc_owner(request, boat_id, owner_id):
  Boat.objects.get(id=boat_id).owners.remove(owner_id)
  return redirect('detail', boat_id=boat_id)