from django.db import models

# Create your models here.
from shortener.models import MyUrlShortner

class ClickEventManager(models.Manager):
    def create_event(self, MyUrlShortnerInstance):
        if isinstance(MyUrlShortnerInstance,MyUrlShortner):
            obj, created = self.get_or_create(kirr_url=MyUrlShortnerInstance)
            if not create:
            	print("current count of clicks: ",obj.count)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
   
    kirr_url    = models.OneToOneField(MyUrlShortner)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True) 
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)