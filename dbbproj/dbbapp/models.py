from django.db import models

# Create your models here.
class Userdb(models.Model):
    name = models.CharField(max_length=20,null=True)
    url = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table ="dbuser"
        
