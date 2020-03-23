from django.db import models

# Create your models here.
# from filer.fields.image import FilerImageField

class Event(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField()
    date = models.DateField()

from cms.models.pluginmodel import CMSPlugin
class TimelinePluginModel(CMSPlugin):
    events = models.ManyToManyField(Event)

    def copy_relations(self, oldinstance):
        self.events.set(oldinstance.events.all())