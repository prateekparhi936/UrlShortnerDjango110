from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View

from .forms import SubmitUrlForm
from .models import MyUrlShortner
from analytics.models import ClickEvent

# Create your views here

def home_view_fbv(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, "shortener/home.html", {})

class UrlShortnerRedirectView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		qs = MyUrlShortner.objects.filter(shortcode__iexact=shortcode)
		if qs.count() != 1 and not qs.exists():
			raise Http404
		obj=qs.first()
		print("count of clicks ",ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)

class HomeView(View):     #class based view
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {"title": "UrlShortener", "form": the_form}
		return render(request,"shortener/home.html",context)

	def post(self,request,*args,**kwargs):
		form=SubmitUrlForm(request.POST)
		if(form.is_valid()):
			print(form.cleaned_data.get("url"))
		context={"title":"UrlShortener","form":form}
		template="shortener/home.html"
		obj=""
		created=False
		if form.is_valid():
			new_url=form.cleaned_data.get("url")
			obj, created=MyUrlShortner.objects.get_or_create(url=new_url)
			context={
				"object":obj,
				"created":created,
			}
		if created:
			template="shortener/success.html"
		else:
			template="shortener/already-exists.html"
		return render(request,template,context)