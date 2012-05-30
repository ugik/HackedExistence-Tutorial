from django.db import models

class HomePage(models.Model):
    homecopy                = models.TextField()
    
    def __unicode__(self):
        return 'Home Page Copy'
        
