from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Drinker(models.Model):
    user            = models.OneToOneField(User)
    birthday      = models.DateField()
    name          = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
        
# create user object attached to drinker object

#def create_drinker_user_callback(sender, instance, **kwargs):
#    drinker, new = Drinker.objects.get_or_create(user=instance)
#post_save.connect(create_drinker_user_callback, User)

