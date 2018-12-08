from django.db import models

from .utils import code_generator, create_newcode
from .validators import validate_url, validate_dot_com
from django_hosts.resolvers import reverse

class MyModelManager(models.Manager):
	def all(self,*args,**kwargs):
		qs_main=super(MyModelManager,self).all(*args,**kwargs)
		qs=qs_main.filter(active=True)
		return qs

	def refresh_shortcode(self,items=None):
		qs=MyUrlShortner.objects.filter(id__gte=1)
		if items is not None and isinstance(items,int):
			qs=qs.order_by('-id')[:items]
		new_codes=0
		for q in qs:
			q.shortcode=create_newcode(q)
			print(q.id)
			q.save()
			new_codes+=1
		return "New_Codes made: {i}".format(i=new_codes)


class MyUrlShortner(models.Model):
	url=models.CharField(max_length=120, validators=[validate_url, validate_dot_com])
	shortcode=models.CharField(max_length=15,unique=True,blank=True)
	active=models.BooleanField(default=True)

	objects=MyModelManager()

	def save(self,*args,**kwargs):
		if self.shortcode=="" or self.shortcode is None:
			self.shortcode= create_newcode(self)
		super(MyUrlShortner,self).save(*args,**kwargs)

	def __str__(self):
		return str(self.url)

