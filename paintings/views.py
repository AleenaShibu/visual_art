from django.shortcuts import render


from django.views.genreic import ListView,DetailView,PermissionRequired
from django.views.generic.edit import DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Painting
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class PaintingListView(ListView):
	model = Painting
	template_name ='home.html'

class PaintingDetailView(DetailView):
	model = Painting
	template_name ='detail.html'

class AddVPaintingview(CreateView):
	model = Painting
	template_name ='addpainting.html'
	fields = ['name','artist_name','subject','origin','medium','image']

class DeletePaintingView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Painting
	template_name = 'delete.html'
	success_url = reverse_lazy('home')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.artist== self.request.user


class SearchPaintingView(ListView):
	model = Painting
	template_name = 'searchview.html'

	def ger_Queryset(self):
		query =self.request.GET['q']
		return.Painting.objects.filter(name__icontains=query)
	