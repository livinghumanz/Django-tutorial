from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    mailid = models.EmailField(max_length=100)
    college = models.TextField()
    contact = models.BigIntegerField()
    loc = models.CharField(max_length=20)
    
    def __str__(self):
        return '{0} from {1}'.format(self.name,self.college)